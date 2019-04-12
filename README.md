# SAFESKY - Weather Forecasting using Machine Learning

#### REST API
**url:** treetrails.herokuapp.com/machinelearning/weatherforecast/`2019-04-05`/<br>
**returns:** `  { 
                  "status":   200,
                  "data":     {
                                "date": "2019-04-05",
                                "tmin": 20.74581885355267,
                                "tmax": 33.60100870778798,
                                "tavg": 27.014038006528352
                              }
                }`

#### DATASET
The weather data of [New Delhi, INDIA](https://www.google.com/maps/place/New+Delhi,+Delhi/@28.5272181,77.0688974,11z/data=!3m1!4b1!4m5!3m4!1s0x390cfd5b347eb62d:0x52c2b7494e204dce!8m2!3d28.6139391!4d77.2090212) was obtained from [**NOAA**](https://www.ncdc.noaa.gov/cdo-web/)(National Oceanic and Atmospheric Administration, USA)

#### ALGORITHM
[**Ridge Regression**](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)

#### Environment setup
1. Download and install [Python3](https://www.python.org).
2. Download all the python packages listed in the `requirements.txt` file using command `pip3 install <package-name>`.

#### How to run
1. Open terminal and execute command: `jupyter-notebook`.
2. Browser window will open with directory structure.
3. Navigate to particular directory(LSTM).
4. Click to open the file `weatherforecast.ipynb`.
5. Click on run icon on top bar to execute the code.
