class Tomaatti(object):
	def __init__(self):
		from os.path import expanduser, exists, join
		from os import makedirs
		from gettext import bindtextdomain, textdomain

		# ensure the root directory for the configuration files exist
		self.__config_directory = expanduser('~/.config/tomaatti')
		if not exists(self.__config_directory):
			makedirs(self.__config_directory)

		# determine the name of some essential configuration files
		self.__config_start_time = join(self.__config_directory, 'start_time.txt')

	def translate_string(self, input_text):
		from gettext import gettext
		return gettext(input_text)

	@property
	def config_start_time(self):
		return self.__config_start_time


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
	def get_clicked_button():
		from os import environ
		if I3Integration.CLICKED_BUTTON_ENVIRON in environ:
			return environ[I3Integration.CLICKED_BUTTON_ENVIRON]
		return None

	@staticmethod
	def get_block_name():
		from os import environ
		if I3Integration.BLOCK_NAME_ENVIRON in environ:
			return environ[I3Integration.BLOCK_NAME_ENVIRON]
		return None

	@staticmethod
	def get_block_instance():
		from os import environ
		if I3Integration.BLOCK_INSTANCE_ENVIRON in environ:
			return environ[I3Integration.BLOCK_INSTANCE_ENVIRON]
		return None
