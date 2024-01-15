import unittest

import testdata.test_testweatherdata as test_testweatherdata

import frcm.datamodel.utils as utils
from frcm.datamodel.model import WeatherData, Observations, Forecast, Location

from frcm.frcapi import FireRiskAPI
from frcm.weatherdata.client_met import METClient
from frcm.weatherdata.extractor_met import METExtractor
from frcm.datamodel.model import Location
import frcm.fireriskmodel.preprocess


class TestFRCAPI(unittest.TestCase):

    def setUp(self):

        met_extractor = METExtractor()

        met_client = METClient(extractor=met_extractor)  # TODO: maybe embed extractor into client

        self.frc = FireRiskAPI(client=met_client)

        wd = test_testweatherdata.sample_wd

        observations_wdps = utils.list_to_wdps(wd['observations']['data'])
        forecast_wdps = utils.list_to_wdps(wd['forecast']['data'])

        # TODO: this mapping from dict to weatherdata could be moved into data model
        observations = Observations(source=wd['observations']['source'],
                                    location=Location(latitude=wd['observations']['location']['latitude'],
                                                      longitude=wd['observations']['location']['longitude']),
                                    data=observations_wdps)

        forecast = Forecast(location=Location(latitude=wd['forecast']['location']['latitude'],
                                              longitude=wd['forecast']['location']['longitude']),
                            data=forecast_wdps)

        self.wd = WeatherData(created=wd['created'],
                              observations=observations,
                              forecast=forecast)

    def test_preprocess(self):

        #print(self.wd.observations)
        #print(self.wd.forecast)

        #frcm.fireriskmodel.preprocess.preprocess(self.wd)

        # for now just check that it runs without errors
        self.assertTrue(True)

    def test_compute(self):

        predictions = self.frc.compute(self.wd)

        print(predictions)

        # for now just check that it runs without errors
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
