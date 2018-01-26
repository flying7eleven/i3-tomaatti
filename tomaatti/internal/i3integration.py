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
