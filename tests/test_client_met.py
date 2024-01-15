import datetime

from frcm.weatherdata.extractor_met import METExtractor
from frcm.weatherdata.client_met import METClient

from frcm.datamodel.model import Location

import unittest


class TestClient(unittest.TestCase):

    def setUp(self):

        self.extractor = METExtractor()

        self.client = METClient(self.extractor)

        self.location = Location(latitude=60.383, longitude=5.3327)

        self.station = 'SN50540'

    def test_fetch_forecast_raw(self):

        response = self.client.fetch_forecast_raw(self.location)

        print(response.text)

        self.assertEqual(response.status_code, 200)

    def test_fetch_forecast(self):

        forecast = self.client.fetch_forecast(self.location)

        print(forecast)

        self.assertTrue(True)

    def test_get_nearest_station_raw(self):

        response = self.client.get_nearest_station_raw(self.location)

        self.assertEqual(response.status_code, 200)

    def test_get_nearest_station_id(self):

        station_id = self.client.get_nearest_station_id(self.location)

        self.assertEqual(self.station, station_id)

    def test_fetch_observations_raw(self):

        start_date = datetime.datetime(year=2022, month=4, day=1)
        end_date = datetime.datetime(year=2022, month=4, day=2)

        response = self.client.fetch_observations_raw(self.station, start_date, end_date)

        print(response.text)

        self.assertEqual(response.status_code, 200)

    def test_fetch_observations(self):

        start_date = datetime.datetime(year=2022, month=4, day=1)
        end_date = datetime.datetime(year=2022, month=4, day=2)

        observations = self.client.fetch_observations(self.location, start=start_date, end=end_date)

        print(observations)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
