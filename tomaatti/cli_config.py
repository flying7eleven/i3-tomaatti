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

    # define the actual argument parser
    argument_parser = ArgumentParser(description='Pomodoro timer for i3 - Configuration tool')

    # now we can start parsing the supplied arguments
    parsed_arguments = argument_parser.parse_args()


if __name__ == '__main__':
    script_entry_point()
