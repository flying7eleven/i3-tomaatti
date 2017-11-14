def script_entry_point():
	from argparse import ArgumentParser
	from tomaatti import I3Integration, Tomaatti

	# define the actual argument parser
	argument_parser = ArgumentParser(description='Pomodoro timer for i3')
	argument_parser.add_argument('-w', '--working-period', type=int, default=25, help='The time you want to work on a project (in minutes).')
	argument_parser.add_argument('-p', '--pause-period', type=int, default=5, help='The time you want to pause between to working periods (in minutes).')
	argument_parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true')

	# now we can start parsing the supplied arguments
	parsed_arguments = argument_parser.parse_args()

	# get an instance of the main class and the alias for the translation function
	app = Tomaatti()
	_ = app.translate_string

	# toggle the timer if the user performed a right-click
	if I3Integration.get_clicked_button() == I3Integration.RIGHT_MOUSE_BUTTON:
		app.toggle_timer()

	# current test output
	if not app.is_running:
		print(_('Click to start pomodoro'))
	else:
		print(_('Pomodoro timer is running'))


if __name__ == '__main__':
	script_entry_point()
