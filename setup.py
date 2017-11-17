# Copyright (C) 2017 Tim Hütz
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not,
# see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
	name='tomaatti',
	version='0.2.0',
	description='Pomodoro timer with i3 integration',
	long_description='Pomodoro timer with i3 integration',
	url='https://github.com/thuetz/i3-tomaatti',
	author='Tim Hütz',
	author_email='tim@huetz.biz',
	license='GPL-3.0',
	packages=find_packages(),
	install_requires=[
		'easygui'
	],
	zip_safe=False,
	platforms=['Linux'],
	entry_points={
		'console_scripts': [
			'tomaatti = tomaatti.cli:script_entry_point',
		],
	}
)
