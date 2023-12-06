import os
import sys
import datetime

import numpy
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

# https://numpy.org/doc/stable/reference/generated/numpy.interp.html
# can we provide all points at the same time so that we do not need to interpolate segmentwise?

def interpolate(x, point1, point2):

    y = numpy.interp(x, [point1[0], point2[0]], [point1[1], point2[1]])

    return y


def interpolate_interval(wd_point1: WeatherDataPoint, wd_point2: WeatherDataPoint, delta: int):

    wdps = list()

    start_time = wd_point1.timestamp
    end_time = wd_point2.timestamp

    segment_width = end_time - start_time

    segment_width_sec = segment_width.total_seconds()

#    print(time_width.total_seconds())

    # generate relative x-times
    # TODO: switch to list-comprehension
    current_time = 0
    times_sec = list()

    while current_time <= segment_width_sec:

        times_sec.append(current_time)
        current_time = current_time + delta

    #print(times_sec)

    temperatures = interpolate(times_sec, [0, wd_point1.temperature], [segment_width_sec, wd_point2.temperature])
    humidities = interpolate(times_sec, [0, wd_point1.humidity], [segment_width_sec, wd_point2.humidity])
    wind_speeds = interpolate(times_sec, [0, wd_point1.wind_speed], [segment_width_sec, wd_point2.wind_speed])

    for i in range(0, len(times_sec)):

        timestamp = start_time + datetime.timedelta(seconds=times_sec[i])
        wd_point = WeatherDataPoint(temperature=temperatures[i],
                                    humidity=humidities[i],
                                    wind_speed=wind_speeds[i],
                                    timestamp=timestamp)

        wdps.append(wd_point)

    # what if point 2 it not at an interpolation boundary?
    # do not interpolate beyond a boundary as we do not know where the next point is
    # so last point generated here is to be included
    # last interpolated point up to and iu
    #wdps.append(wd_point2)

    return wdps


def interpolate_wdps(wd_points: list[WeatherDataPoint], delta: int) -> list[WeatherDataPoint]:

    # TODO: first check that data is sorted in ascending order on timestamp
    # and contains at least two points
    # TODO: do we insists on alignment with full hours?

    current_wdp = wd_points[0] # assumes that it is sorted

    wdps = list()
    wdps.append(current_wdp)

    for i in range(1, len(wd_points)):

        next_wdp = wd_points[i]

        interval_wdps = interpolate_interval(current_wdp, next_wdp, delta)

        # TODO: check that we need get some points

        current_wdp = interval_wdps[-1]

        wdps.extend(interval_wdps[1:]) # first point was inserted in previous iteration

    return wdps


if __name__ == "__main__":

    y = interpolate([1, 2], (1, 2), (5, 6))

    print(y)
