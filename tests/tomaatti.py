# Copyright (C) 2017 Tim Hütz
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not,
# see <http://www.gnu.org/licenses/>.

from tomaatti.internal.tomaatti import Tomaatti
from unittest import TestCase
from unittest.mock import patch, MagicMock


class TomaattiTest(TestCase):
	def testCreateFullConfigIfItDoesNotExists(self):
		with patch('os.path.exists') as exists_patch:
			exists_patch.return_value = False

			test_object = Tomaatti()
			test_object._create_initial_config = MagicMock()
			test_object.initialize()

			self.assertTrue(test_object._create_initial_config.has_been_called())
