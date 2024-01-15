import unittest
import datetime

import os
import sys

#current = os.path.dirname(os.path.realpath(__file__))
#parent = os.path.dirname(current)
#sys.path.append(parent)

import frcm.datamodel.model as dm

import testdata.test_testdata_datamodel as test_testdata

import frcm.datamodel.utils as utils


class TestDataModel(unittest.TestCase):

    def setUp(self):
        self.observations_wdps = utils.list_to_wdps(test_testdata.frost_sample_weatherdatapoints)
        self.forecast_wdps = utils.list_to_wdps(test_testdata.met_sample_weatherdatapoints)

    def test_validate(self):
        timedelta_ok = datetime.timedelta(minutes=70)
        timedelta_nok = datetime.timedelta(minutes=30)

        location = dm.Location(latitude=60.383, longitude=5.3327)

        observations = dm.Observations(
            source="testdata",
            location=location,
            data=self.observations_wdps)

        forecast = dm.Forecast(
            location=location,
            data=self.forecast_wdps)

        weatherdata = dm.WeatherData(
            created=datetime.datetime.now(),
            observations=observations,
            forecast=forecast)

        self.assertTrue(utils.wd_validate(weatherdata, timedelta_ok))
        self.assertFalse(utils.wd_validate(weatherdata, timedelta_nok))


if __name__ == '__main__':
    unittest.main()
