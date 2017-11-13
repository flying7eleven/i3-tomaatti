if __name__ == '__main__':
	from argparse import ArgumentParser

	# define the actual argument parser
	argumentParser = ArgumentParser(description='Pomodoro timer for i3')
	argumentParser.add_argument('-w', '--working-period', type=int, default=25, help='The time you want to work on a project (in minutes).')
	argumentParser.add_argument('-p', '--pause-period', type=int, default=5, help='The time you want to pause between to working periodes (in minutes).')
	argumentParser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true')

	# now we can start parsing the supplied arguments
	parsedArguments = argumentParser.parse_args()
