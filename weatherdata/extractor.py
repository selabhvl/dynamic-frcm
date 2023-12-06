import os
import sys

import abc

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from datamodel.model import Observations, Forecast


class Extractor:
    @abc.abstractmethod
    def extract_observations(self, data: str) -> Observations:
        pass

    @abc.abstractmethod
    def extract_forecast(self, data: str) -> Forecast:
        pass



