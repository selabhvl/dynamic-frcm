import unittest
import datetime
import dateutil

import testdata.test_testdata_fireriskmodel as test_testdata

import frcm.datamodel.utils as utils


class TestUtil(unittest.TestCase):

    def setUp(self):
        self.observations_wdps = utils.list_to_wdps(test_testdata.frost_sample_weatherdatapoints)
        self.forecast_wdps = utils.list_to_wdps(test_testdata.met_sample_weatherdatapoints)

    def test_min_time(self):
        min_time = utils.min_time(self.observations_wdps)

        exp_min_time = dateutil.parser.parse('2022-04-01 00:00:00+00:00')

        self.assertEqual(exp_min_time, min_time)

    def test_max_time(self):
        max_time = utils.max_time(self.observations_wdps)

        exp_max_time = dateutil.parser.parse('2022-04-01 23:00:00+00:00')

        self.assertEqual(exp_max_time, max_time)

    def test_is_sorted(self):
        self.assertTrue(utils.is_sorted(self.observations_wdps))
        self.assertTrue(utils.is_sorted(self.forecast_wdps))

        self.assertTrue(utils.is_sorted(list()))

    def test_within_timedelta(self):
        timedelta_ok = datetime.timedelta(minutes=70)
        timedelta_nok = datetime.timedelta(minutes=30)

        self.assertTrue(utils.within_timedelta(self.observations_wdps, timedelta_ok))
        self.assertFalse(utils.within_timedelta(self.forecast_wdps, timedelta_nok))


if __name__ == '__main__':
    unittest.main()
