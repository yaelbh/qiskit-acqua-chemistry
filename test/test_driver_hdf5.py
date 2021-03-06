# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

import unittest
from collections import OrderedDict

from test.common import QiskitAquaChemistryTestCase
from qiskit_aqua_chemistry.drivers import ConfigurationManager
from test.test_driver import TestDriver


class TestDriverHDF5(QiskitAquaChemistryTestCase, TestDriver):
    """HDF5 Driver tests."""

    def setUp(self):
        cfg_mgr = ConfigurationManager()
        hdf5_cfg = OrderedDict([
            ('hdf5_input', self._get_resource_path('test_driver_hdf5.hdf5'))
        ])
        section = {'properties': hdf5_cfg}
        driver = cfg_mgr.get_driver_instance('HDF5')
        self.qmolecule = driver.run(section)


if __name__ == '__main__':
    unittest.main()
