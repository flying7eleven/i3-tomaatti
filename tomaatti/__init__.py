class I3Integration(object):
	CLICKED_BUTTON_ENVIRON = 'BLOCK_BUTTON',
	BLOCK_NAME_ENVIRON = 'BLOCK_NAME',
	BLOCK_INSTANCE_ENVIRON = 'BLOCK_INSTANCE',

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
