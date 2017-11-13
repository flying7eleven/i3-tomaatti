def script_entry_point():
	from argparse import ArgumentParser
	from tomaatti import I3Integration

	# define the actual argument parser
	argument_parser = ArgumentParser(description='Pomodoro timer for i3')
	argument_parser.add_argument('-w', '--working-period', type=int, default=25, help='The time you want to work on a project (in minutes).')
	argument_parser.add_argument('-p', '--pause-period', type=int, default=5, help='The time you want to pause between to working periods (in minutes).')
	argument_parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true')

	# now we can start parsing the supplied arguments
	parsed_arguments = argument_parser.parse_args()

	print('i3', I3Integration.get_block_name())


if __name__ == '__main__':
	script_entry_point()
