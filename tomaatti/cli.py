# Copyright (C) 2017 Tim Hütz
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
	from tomaatti import I3Integration, Tomaatti

	# define the actual argument parser
	argument_parser = ArgumentParser(description='Pomodoro timer for i3')

	# now we can start parsing the supplied arguments
	parsed_arguments = argument_parser.parse_args()

	# get an instance of the main class
	app = Tomaatti()

	# toggle the timer if the user performed a right-click
	if I3Integration.get_clicked_button() == I3Integration.RIGHT_MOUSE_BUTTON:
		app.toggle_timer()

	# print the current label to the console
	print(app.current_label)


if __name__ == '__main__':
	script_entry_point()
