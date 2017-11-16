# Copyright (C) 2017 Tim Hütz
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not,
# see <http://www.gnu.org/licenses/>.

from enum import Enum


class TimerType(Enum):
	WORKING = 1,
	BREAK = 2,
	UNKNOWN = -1


class Tomaatti(object):
	def __init__(self):
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
		self._application_config = ConfigParser()
		if exists(self._config_app_state):
			self._application_config.read(self._config_app_state)

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
	def current_timer_type(self) -> int:
		val = self._application_config.getint('timer', 'mode', fallback=1)
		return val

	@current_timer_type.setter
	def current_timer_type(self, value: int):
		self._application_config.set('timer', 'mode', str(value))
		self._persist_current_state()

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
		if not self.is_running:
			return 'Click to start pomodoro'
		else:
			from datetime import datetime, time
			time_to_end = datetime.strptime(self.end_time, '%Y-%m-%d %H:%M:%S') - datetime.now()
			return '{:02}:{:02}'.format(time_to_end.seconds % 3600 // 60, time_to_end.seconds % 60)

	def toggle_timer(self) -> None:
		from datetime import datetime, timedelta

		# toggle the current state
		self._application_config.set('timer', 'is_running', ConfigHelper.bool_to_config_str(not self.is_running))

		# if we started the timer, set the target time accordingly
		if self.is_running:
			current_time = datetime.now()
			period = self.working_period
			if 2 == self.current_timer_type:
				period = self.break_period
			time_period = timedelta(minutes=period)
			end_time = current_time + time_period
			self._application_config.set('timer', 'end_time', end_time.strftime('%Y-%m-%d %H:%M:%S'))

		# save all changes to the configuration file
		self._persist_current_state()

	def show_message(self, message: str) -> None:
		from easygui import msgbox
		msgbox(message, Tomaatti.translate_string('Tomaatti'))

	def _persist_current_state(self) -> None:
		with open(self._config_app_state, 'w') as configfile:
			self._application_config.write(configfile)

	def check_state(self):
		if self.is_running and self.is_timer_up:
			self.toggle_timer()
			if 1 == self.current_timer_type:
				self.show_message('Work period is up!')
				self.current_timer_type = 2
			elif 2 == self.current_timer_type:
				self.show_message('Break period is up!')
				self.current_timer_type = 1
			else:
				self.show_message('ERROR: %s' % str(self.current_timer_type))
			self.toggle_timer()


class ConfigHelper(object):
	@staticmethod
	def bool_to_config_str(input_val: bool) -> str:
		if input_val:
			return 'yes'
		return 'no'


class I3Integration(object):
	CLICKED_BUTTON_ENVIRON = 'BLOCK_BUTTON'
	BLOCK_NAME_ENVIRON = 'BLOCK_NAME'
	BLOCK_INSTANCE_ENVIRON = 'BLOCK_INSTANCE'
	LEFT_MOUSE_BUTTON = 1
	MIDDLE_MOUSE_BUTTON = 2
	RIGHT_MOUSE_BUTTON = 3
	MOUSE_SCROLL_UP = 4
	MOUSE_SCROLL_DOWN = 5

	@staticmethod
	def get_clicked_button() -> int:
		from os import environ
		if I3Integration.CLICKED_BUTTON_ENVIRON in environ:
			try:
				return int(environ[I3Integration.CLICKED_BUTTON_ENVIRON])
			except ValueError:
				return -1
		return -1

	@staticmethod
	def get_block_name() -> str:
		from os import environ
		if I3Integration.BLOCK_NAME_ENVIRON in environ:
			return environ[I3Integration.BLOCK_NAME_ENVIRON]
		return ''

	@staticmethod
	def get_block_instance() -> str:
		from os import environ
		if I3Integration.BLOCK_INSTANCE_ENVIRON in environ:
			return environ[I3Integration.BLOCK_INSTANCE_ENVIRON]
		return ''
