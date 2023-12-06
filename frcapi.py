import datetime

from datamodel.model import FireRiskPrediction, Location, WeatherData, Observations, Forecast
from weatherdata.client import WeatherDataClient
from datamodel.utils import wd_validate, wdps_list_str
import fireriskmodel.compute

import weatherdata.utils


class FireRiskAPI:

    def __init__(self, client: WeatherDataClient):
        self.client = client
        self.timedelta_ok = datetime.timedelta(days=1) # TODO: when during a day is observations updated? (12:00 and 06:00)
        # TODO (NOTE): Short term forecast updates every 3rd hour with long term forecast every 12th hour at 12:00 and 06:00
        self.interpolate_distance = 720

    def compute(self, wd: WeatherData) -> FireRiskPrediction:

        return fireriskmodel.compute.compute(wd)

    def preprocess(self, wd: WeatherData):

        # validate order, max timedelta and gap between observation and forecast
        validated = wd_validate(wd, self.timedelta_ok)

        print(validated)

        # interpolate
        obs_wdps_interpolated = weatherdata.utils.interpolate_wdps(wd.observations.data, self.interpolate_distance)
        fct_wdps_interpolated = weatherdata.utils.interpolate_wdps(wd.forecast.data, self.interpolate_distance)

        wd_interpolated = WeatherData(created=wd.created,
                                      observations=Observations(source=wd.observations.source,
                                                                location=wd.observations.location,
                                                                data=obs_wdps_interpolated),
                                      forecast=Forecast(location=wd.forecast.location,
                                                        data=fct_wdps_interpolated))
        #print(wd_interpolated.observations)
        #print(wd_interpolated.forecast)

        latest_obs = wd_interpolated.observations.data[-1]

        #print(latest_obs)

        earliest_fct = wd_interpolated.forecast.data[0]

        #print(earliest_fct)

        gap = [latest_obs, earliest_fct]

        gap_interpolated = weatherdata.utils.interpolate_wdps(gap, self.interpolate_distance)

        # for now all gap wdps goes into observations

        gap_observations = gap_interpolated[1:-1]

        wd_interpolated.observations.data.extend(gap_observations)

        #print(wd_interpolated.observations)
        #print(wd_interpolated.forecast)

        #print(wdps_list_str(gap_observations))

        #print(latest_obs)

        #print(earliest_fct)

        return wd_interpolated


    def compute_now(self, location: Location, obs_delta: datetime.timedelta) -> FireRiskPrediction:

        time_now = datetime.datetime.now()
        start_time = time_now - obs_delta

 #       print(time_now)
 #       print(start_time)

        observations = self.client.fetch_observations(location, start=start_time, end=time_now)

        print(observations)

        forecast = self.client.fetch_forecast(location)

        print(forecast)

        wd = WeatherData(created=time_now, observations=observations, forecast=forecast)

        print(wd.to_json())

 #       print(wd)

        # wd_preprocessed = self.preprocess(wd)# TODO (NOTE): turned off during testing (moving interpolation to frm)

        # print(wd_preprocessed.observations)

        # print(wd_preprocessed.forecast)

        prediction = self.compute(wd) # TODO (NOTE): is rewritten from wd_preprocessed to wd for testing

        return prediction

        # compute firerisks based on weather data

        # return firerisks



    def compute_now_period(self, location: Location, obs_delta: datetime.timedelta, fct_delta: datetime.timedelta):
        pass

    def compute_period(self, location: Location, start: datetime, end: datetime) -> FireRiskPrediction:
        pass

    def compute_period_delta(self, location: Location, start: datetime, delta: datetime.timedelta) -> FireRiskPrediction:
        pass


