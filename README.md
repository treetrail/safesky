# SAFESKY - Weather Forecasting using Machine Learning

Implementation of different machine learning techniques for weather forecasting.
#### REST API
**url:** tsweatherapi.herokuapp.com/forecast/`yyyy-mm-dd`/<br>
**returns:** `{"date": "yyyy-mm-dd", "avgTemp": "float"}`
##### Dataset
The weather data of [New Delhi, INDIA](https://www.google.com/maps/place/New+Delhi,+Delhi/@28.5272181,77.0688974,11z/data=!3m1!4b1!4m5!3m4!1s0x390cfd5b347eb62d:0x52c2b7494e204dce!8m2!3d28.6139391!4d77.2090212) was obtained from [**NOAA**](https://www.ncdc.noaa.gov/cdo-web/)(National Oceanic and Atmospheric Administration, USA) 
##### ML Techniques
1. [**Ridge Regression**](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)
2. [**ARIMA**](https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/)
3. [**LSTM**](https://keras.io/layers/recurrent/#lstm)


## Environment setup

1. Download and install [Python3](https://www.python.org).
2. Download all the python packages listed in the `requirements.txt` file using command `pip3 install <package-name>`.


## How to run

There are three techniques used to serve the purpose individually. **Ridge Regression**, **ARIMA**(AutoRegressive Integrated Moving Average) and **LSTM**(Long Short Term Memory)

### RIDGE and ARIMA -
1. Open the terminal and move to the particular directory.
2. Execute: `python3 <file-name>.py`.

### LSTM - 
1. Open terminal and execute command: `jupyter-notebook`.
2. Browser window will open with directory structure.
3. Navigate to particular directory(LSTM).
4. Click to open the file `weather_n.ipynb`.
5. Click on run icon on top bar to execute the code. 
