# Copyright (C) 2017 Tim Hütz
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not,
# see <http://www.gnu.org/licenses/>.

class Tomaatti(object):
	TIMER_TYPE_WORKING = 1
	TIMER_TYPE_BREAK = 2

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
	def translate_string(input_text) -> str:
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
		return self._application_config.getint('timer', 'mode', fallback=Tomaatti.TIMER_TYPE_WORKING)

	def toggle_timer(self) -> None:
		self._application_config.set('timer', 'is_running', ConfigHelper.bool_to_config_str(not self.is_running))
		self._persist_current_state()

	def show_message(self, message: str) -> None:
		from easygui import msgbox
		msgbox(message, Tomaatti.translate_string('Tomaatti'))

	def _persist_current_state(self) -> None:
		with open(self._config_app_state, 'w') as configfile:
			self._application_config.write(configfile)


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
