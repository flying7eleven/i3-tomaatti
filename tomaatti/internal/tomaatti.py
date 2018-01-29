# -*- coding: utf-8 -*-
# Copyright (C) 2017 - 2018 Tim Hütz
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not,
# see <http://www.gnu.org/licenses/>.
from tomaatti import ScreenOverlay
from .confighelper import ConfigHelper
from .timertype import TimerType


class Tomaatti(object):
	def initialize(self, configuration_parser=None):
		from os.path import expanduser, exists, join
		from os import makedirs
		from configparser import ConfigParser

		# ensure the root directory for the configuration files exist
		self._config_directory = expanduser('~/.config/tomaatti')
		if not exists(self._config_directory):
			makedirs(self._config_directory)

		# determine the name of some essential configuration files
		self._config_app_state = join(self._config_directory, 'application_state.ini')

		# if a configuration file exists, read it
		if configuration_parser:
			self._application_config = configuration_parser
		else:
			self._application_config = ConfigParser()
		if exists(self._config_app_state):
			self._application_config.read(self._config_app_state)
		else:
			self._create_initial_config()

	@staticmethod
	def translate_string(input_text: str) -> str:
		from gettext import gettext, bindtextdomain, textdomain
		bindtextdomain('tomaatti', '/path/to/my/language/directory')  # TODO set a correct path
		textdomain('tomaatti')
		return gettext(input_text)

	@property
	def is_running(self) -> bool:
		return self._application_config.getboolean('timer', 'is_running', fallback=False)

	@property
	def working_period(self) -> int:
		return self._application_config.getint('periods', 'working', fallback=25)

	@property
	def break_period(self) -> int:
		return self._application_config.getint('periods', 'break', fallback=5)

	@property
	def current_timer_type(self) -> TimerType:
		val = self._application_config.getint('timer', 'mode')
		if 1 == val:
			return TimerType.WORKING
		elif 2 == val:
			return TimerType.BREAK
		else:
			return TimerType.UNKNOWN

	@current_timer_type.setter
	def current_timer_type(self, value: TimerType):
		if TimerType.WORKING == value:
			self._application_config.set('timer', 'mode', '1')
		elif TimerType.BREAK == value:
			self._application_config.set('timer', 'mode', '2')
		else:
			self._application_config.set('timer', 'mode', '-1')
		self._persist_current_state()

	@property
	def use_expermental_overlay(self):
		return self._application_config.getboolean('experimental', 'overlay', fallback=False)

	@property
	def end_time(self) -> str:
		from datetime import datetime
		return self._application_config.get('timer', 'end_time', fallback=str(datetime.now()))

	@property
	def is_timer_up(self) -> bool:
		from datetime import datetime
		time_to_end = datetime.strptime(self.end_time, '%Y-%m-%d %H:%M:%S') - datetime.now()
		return time_to_end.days < 0

	@property
	def current_label(self) -> str:
		# determine a prefix for the bar
		prefix = ''
		if self.use_font_awesome:
			prefix = '&#xf017;  '

		# determine the actual label for the bar
		if not self.is_running:
			return '{}{}'.format(prefix, self.translate_string('Tomaatti'))
		else:
			from datetime import datetime
			time_to_end = datetime.strptime(self.end_time, '%Y-%m-%d %H:%M:%S') - datetime.now()
			return '{}{:02}:{:02}'.format(prefix, time_to_end.seconds % 3600 // 60, time_to_end.seconds % 60)

	def toggle_timer(self) -> None:
		from datetime import datetime, timedelta

		# toggle the current state
		self._application_config.set('timer', 'is_running', ConfigHelper.bool_to_config_str(not self.is_running))

		# if we started the timer, set the target time accordingly
		if self.is_running:
			current_time = datetime.now()
			period = self.working_period
			if TimerType.BREAK == self.current_timer_type:
				period = self.break_period
			time_period = timedelta(minutes=period)
			end_time = current_time + time_period
			self._application_config.set('timer', 'end_time', end_time.strftime('%Y-%m-%d %H:%M:%S'))

		# save all changes to the configuration file
		self._persist_current_state()

	def show_message(self, message: str) -> None:
		if not self.use_expermental_overlay:
			from easygui import msgbox
			msgbox(message, Tomaatti.translate_string('Tomaatti'))
		else:
			overlay = ScreenOverlay()
			overlay.show_overlay(message)

	def _persist_current_state(self) -> None:
		with open(self._config_app_state, 'w') as configfile:
			self._application_config.write(configfile)

	def check_state(self):
		if self.is_running and self.is_timer_up:
			self.toggle_timer()
			if TimerType.WORKING == self.current_timer_type:
				self.show_message(self.translate_string(
					"It's time for a break. You worked so hard for the last %d minutes :)" % self.working_period))
				self.current_timer_type = TimerType.BREAK
			elif TimerType.BREAK == self.current_timer_type:
				self.show_message(self.translate_string(
					"You had %d minutes of break. Time to start working again!" % self.break_period))
				self.current_timer_type = TimerType.WORKING
			else:
				self.show_message(self.translate_string('ERROR: %s') % str(self.current_timer_type))
			self.toggle_timer()

	def switch_mode(self):
		was_running = False
		if self.is_running:
			self.toggle_timer()
			was_running = True
		if TimerType.WORKING == self.current_timer_type:
			self.current_timer_type = TimerType.BREAK
		else:
			self.current_timer_type = TimerType.WORKING
		if was_running:
			self.toggle_timer()

	def _create_initial_config(self):
		self._application_config.add_section('timer')
		self._application_config.add_section('periods')
		self._application_config.add_section('ui')
		self.current_timer_type = TimerType.WORKING
		self.working_period = 25
		self.break_period = 5
		self.toggle_timer()  # two times is...
		self.toggle_timer()  # ...intentionally
		self._persist_current_state()

	@break_period.setter
	def break_period(self, value):
		self._application_config.set('periods', 'break', str(value))

	@working_period.setter
	def working_period(self, value):
		self._application_config.set('periods', 'working', str(value))

	@property
	def use_font_awesome(self) -> bool:
		from configparser import NoSectionError, NoOptionError
		try:
			return self._application_config.getboolean('ui', 'fontawesome')
		except (NoSectionError, NoOptionError, ValueError) as e:
			return False

	@use_font_awesome.setter
	def use_font_awesome(self, value: bool):
		self._application_config.set('ui', 'fontawesome', ConfigHelper.bool_to_config_str(value))
