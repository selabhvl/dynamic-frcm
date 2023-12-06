import unittest
import datetime

import sampledata.frost_sample_weatherdata
import sampledata.met_sample_weatherdata

import utils


class TestUtil(unittest.TestCase):

    def setUp(self):
        self.observation_wdps = \
            utils.weatherdata_parse(sampledata.frost_sample_weatherdata.frost_sample_weatherdata['data'])

        self.forecast_wdps = \
            utils.weatherdata_parse(sampledata.met_sample_weatherdata.met_sample_weatherdata['data'])

    def test_interpolate_obs(self):

        print("Observations")
        interpolated_obs_wdps = utils.interpolate_wdps(self.observation_wdps, 720)

        for wdp in interpolated_obs_wdps:
            print(wdp)

        for i in range(1, len(interpolated_obs_wdps)):
            timedelta = \
                interpolated_obs_wdps[i].timestamp - interpolated_obs_wdps[i-1].timestamp

            self.assertEqual(timedelta, datetime.timedelta(seconds=720))

    def test_interpolate_fct(self):

        print("Forecast")
        interpolated_fct_wdps = utils.interpolate_wdps(self.forecast_wdps, 720)

        for wdp in interpolated_fct_wdps:
            print(wdp)

        for i in range(1, len(interpolated_fct_wdps)):
            timedelta = \
                interpolated_fct_wdps[i].timestamp - interpolated_fct_wdps[i - 1].timestamp

        self.assertEqual(timedelta, datetime.timedelta(seconds=720))


if __name__ == '__main__':
    unittest.main()
