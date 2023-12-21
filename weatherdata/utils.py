import os
import sys
import dateutil.parser

# https://www.geeksforgeeks.org/python-import-from-parent-directory/
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from datamodel.model import WeatherDataPoint


def weatherdata_parse(datadict) -> list[WeatherDataPoint]:

    data = list()

    for item in datadict:

        temperature = item['temperature']
        humidity = item['humidity']
        wind_speed = item['wind_speed']
        timestamp = dateutil.parser.parse(item['timestamp'])

        wd_point = WeatherDataPoint(temperature=temperature,
                                    humidity=humidity,
                                    wind_speed=wind_speed,
                                    timestamp=timestamp)

        data.append(wd_point)

    return data

