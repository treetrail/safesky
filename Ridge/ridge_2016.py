import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

class WeatherForecasting:
    def __init__(self, date):
        self.target = date
    def dayOfYear(self, date):
        test_date_str_list = date.split('-')
        test_date = datetime.date(int(test_date_str_list[0]), int(test_date_str_list[1]), int(test_date_str_list[2]))
        return test_date.timetuple().tm_yday

    def forecast(self):
        global model
        ret = {}
        ret['date'] = self.target
        result = self.trainAndForecast(self.target)
        ret['Average Temperature in Celsius'] = result[0][0]
        print(ret)

    def trainAndForecast(self, date):
        filename = 'ndls2016.csv'
        file = np.array(pd.read_csv(filename, header=0))
        x = np.array([])
        y = np.array([])
        for i in file:
            temp_date_day_of_year = self.dayOfYear(i[1])
            temp_date_tavg = i[2]
            x = np.append(x, temp_date_day_of_year)
            y = np.append(y, temp_date_tavg)
        x = x.reshape(-1, 1)
        y = y.reshape(-1, 1)
        plt.plot(x,y)
        model = make_pipeline(PolynomialFeatures(degree=2), Ridge())
        model.fit(x, y)
        yday = self.dayOfYear(date)
        temp_yday = model.predict(yday)
        # Actual
        print('Actual Temperature : ', y[yday])
        plt.scatter(yday, y[yday], color='Green', label='Actual')
        # Predicted
        print('Forecast : ', temp_yday)
        plt.scatter(yday, temp_yday, color='Red', label='Forecast')
        plt.legend(loc='best')
        plt.title('Forecast for ' + date)
        plt.show()
        return model.predict(yday)

def main():
    date = '2017-1-26'
    print('Checking for date : ', date)
    x = WeatherForecasting(date)
    x.forecast()
    print('Done')

if __name__=="__main__":
    main()
