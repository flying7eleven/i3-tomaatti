# Copyright (C) 2017 - 2018 Tim Hütz
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
	version='0.4.0',
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
	classifiers=[
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Environment :: X11 Applications',
		'Topic :: Desktop Environment :: Window Managers',
		'Topic :: Utilities',
		'Development Status :: 3 - Alpha'
	],
	entry_points={
		'console_scripts': [
			'tomaatti = tomaatti.cli:script_entry_point',
		],
	}
)
