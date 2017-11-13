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

	# current test output
	print(_('Click to start pomodoro'))


if __name__ == '__main__':
	script_entry_point()
