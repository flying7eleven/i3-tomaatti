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

from unittest import TestCase
from unittest.mock import patch, MagicMock, call

from tomaatti.internal.tomaatti import Tomaatti, TimerType


class TomaattiTest(TestCase):
	@patch('os.path.exists')
	@patch('os.makedirs')
	def testCreateFullConfigIfItDoesNotExists(self, makedirs_patch, patch_exists):
		patch_exists.return_value = False
		makedirs_patch.return_value = None

		config_mock = MagicMock()

		test_object = Tomaatti()
		test_object.toggle_timer = MagicMock()
		test_object._persist_current_state = MagicMock()
		test_object.initialize(config_mock)

		config_mock.add_section.assert_has_calls([call('timer'), call('ui'), call('periods')], any_order=True)
		config_mock.assert_has_calls([
			call.set('timer', 'mode', str(TimerType.WORKING.value[0])),
			call.set('periods', 'working', '25'),
			call.set('periods', 'break', '5')],
			any_order=True)

	@patch('os.path.exists')
	def testReadConfigIfItExists(self, patch_exists):
		patch_exists.return_value = True

		test_object = Tomaatti()
		test_object._create_initial_config = MagicMock()
		test_object.initialize(MagicMock())

		test_object._create_initial_config.assert_not_called()
		test_object._application_config.read.assert_called()
