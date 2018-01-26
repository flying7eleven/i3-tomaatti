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

def script_entry_point():
	from argparse import ArgumentParser
	from tomaatti import I3Integration, Tomaatti, ScreenOverlay

	# define the actual argument parser
	argument_parser = ArgumentParser(description='Pomodoro timer for i3')
	argument_parser.add_argument('--screen-overlay', action='store_true', help='Show a full screen overlay (experimental)')
	argument_parser.add_argument('--blur-overlay', action='store_true', help='Blur the background of the screen overlay (experimental)')

	# now we can start parsing the supplied arguments
	parsed_arguments = argument_parser.parse_args()

	# show the experimental screen overlay if the user requested it
	if parsed_arguments.screen_overlay:
		if ScreenOverlay.is_coposite_manager_running():
			print('Showing screen overlay')
			overlay = ScreenOverlay()
			overlay.show_overlay('This is an experimental feature of Tomaatti')
		else:
			print('Composite manager is not running!')
		return

	# get an instance of the main class
	app = Tomaatti()
	app.initialize()

	# toggle the timer if the user performed a right-click
	if I3Integration.get_clicked_button() == I3Integration.RIGHT_MOUSE_BUTTON:
		app.switch_mode()
	elif I3Integration.get_clicked_button() == I3Integration.LEFT_MOUSE_BUTTON:
		app.toggle_timer()

	# check the timer state and react to it
	app.check_state()

	# print the current label to the console
	print(app.current_label)


if __name__ == '__main__':
	script_entry_point()
