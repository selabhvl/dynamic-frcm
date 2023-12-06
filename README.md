# DYNAMIC Fire risk indicator implementation

This repository contains the implementation of the dynamic fire risk indicator described in the submitted paper:

R.D: Strand and L.M. Kristensen. *An implementation, evaluation and validation of a dynamic fire and conflagration risk indicator for wooden homes*. Submitted for review.

which uses forecast and weather data observation for computing fire risk indication in the form of time-to-flash-over (ttf) for wooden houses. 

# Installation

To install the required Python packages use:

```
pip install -r requirement.txt 
```
# Overview

The implementation is organised into the following main folders:

- `datamodel` - contains an implementation of the data model used for weather data and fire risk indications
- `weatherdata`  contains an client implementations and interfaces for fetching weather data from cloud services.
- `fireriskmodel` contains an implementation of the underlying fire risk model

The main API for the implementation is in the file `frcapi.py`

# Weather Data Sources

The implementation has been designed to be independent of any particular cloud-based weather data service. 

This library contains an implementation that use the weather data services provided by the Norwegian Meteorological Institute (MET)

Specifically, the files `weatherdata/client_met` and `weatherdata/extractor_met.py` shows how to implement client and extractors using

- MET Frost API for weather data observations: https://frost.met.no/index.html
- MET Forecasting API for weather data forecasts: https://api.met.no/weatherapi/locationforecast/2.0/documentation 

To use these pre-implemented clients a file name `.env` must be put into the `weatherdata` folder having the following content:

```
MET_CLIENT_ID = '<INSERT CLIENT ID HERE>'
MET_CLIENT_SECRET = '<INSERT CLIENT SECRET HERE>'
```

Credentials for using the MET APIs can be obtained via: https://frost.met.no/auth/requestCredentials.html

Please make sure that you conform to the terms of service which includes restrictions on the number of API calls.

# Application integration

The file `main.py` provides sample code on how to compute fire risk indications and how to integration the implementation of fire risk indications into applications.


