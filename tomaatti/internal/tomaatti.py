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
from .configuration import Configuration
from .timertype import TimerType


class Tomaatti(object):
	def initialize(self, configuration_parser=None):
		self._config = Configuration(configuration_parser)

	@staticmethod
	def translate_string(input_text: str) -> str:
		from gettext import gettext, bindtextdomain, textdomain
		bindtextdomain('tomaatti', '/path/to/my/language/directory')  # TODO set a correct path
		textdomain('tomaatti')
		return gettext(input_text)

	@property
	def is_timer_up(self) -> bool:
		from datetime import datetime
		time_to_end = self._config.end_time - datetime.now()
		return time_to_end.days < 0

	@property
	def current_label(self) -> str:
		# determine a prefix for the bar
		prefix = ''
		if self._config.use_fontawesome:
			prefix = '&#xf017;  '

		# determine the actual label for the bar
		if not self._config.is_running:
			return '{}{}'.format(prefix, self.translate_string('Tomaatti'))
		else:
			from datetime import datetime
			time_to_end = self._config.end_time - datetime.now()
			return '{}{:02}:{:02}'.format(prefix, time_to_end.seconds % 3600 // 60, time_to_end.seconds % 60)

	def toggle_timer(self) -> None:
		from datetime import datetime, timedelta

		# toggle the current state
		self._config.is_running = not self._config.is_running

		# if we started the timer, set the target time accordingly
		if self._config.is_running:
			current_time = datetime.now()
			period = self._config.work_duration
			if TimerType.BREAK == self._config.mode:
				period = self._config.break_duration
			time_period = timedelta(minutes=period)
			end_time = current_time + time_period
			self._config.end_time = end_time

	def show_message(self, message: str) -> None:
		if not self._config.use_overlay:
			from easygui import msgbox
			msgbox(message, Tomaatti.translate_string('Tomaatti'))
		else:
			overlay = ScreenOverlay()
			overlay.show_overlay(message)

	def check_state(self):
		if self._config.is_running and self.is_timer_up:
			self.toggle_timer()
			if TimerType.WORKING == self._config.mode:
				self.show_message(self.translate_string(
					"It's time for a break. You worked so hard for the last %d minutes :)" % self._config.work_duration))
				self._config.mode = TimerType.BREAK
			elif TimerType.BREAK == self._config.mode:
				self.show_message(self.translate_string(
					"You had %d minutes of break. Time to start working again!" % self._config.break_duration))
				self._config.mode = TimerType.WORKING
			else:
				self.show_message(self.translate_string('ERROR: %s') % str(self._config.mode))
			self.toggle_timer()

	def switch_mode(self):
		was_running = False
		if self._config.is_running:
			self.toggle_timer()
			was_running = True
		if TimerType.WORKING == self._config.mode:
			self._config.mode = TimerType.BREAK
		else:
			self._config.mode = TimerType.WORKING
		if was_running:
			self.toggle_timer()