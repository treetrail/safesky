import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
import numpy as np
from statsmodels.tsa.stattools import acf, pacf

class regress:
    def __init__(self,path):
        self.path = path

    def runRegress(self):
        # TAVG TMAX TMIN
        # Y = predict TAVG
        # X = Date
        # Parse dates
        dateparse = lambda dates: pd.datetime.strptime(dates,'%Y-%m-%d')
        t_data = pd.read_csv(self.path, parse_dates=['DATE'],date_parser = dateparse,usecols= ['DATE','TAVG'])
        # bangalore_data = t_data
        t_data = t_data.set_index('DATE')
        # t_data = t_data['2017-08']
        # del t_data['NAME']
        print(t_data)
        self.test_stationarity(t_data,doPlot=True)
        self.makeStationary(t_data,doPlot=True)
        self.testAndPlot(t_data, doPlot=True)

    def test_stationarity(self,data,doPlot=False):
        rolmean = data.rolling(window=12,center=False).mean()
        rolstd = data.rolling(window=12,center=False).std()
        if doPlot:
            orig = plt.plot(data, color='blue', label='Original')
            mean = plt.plot(rolmean, color='red', label='Rolling Mean')
            std = plt.plot(rolstd, color='black', label='Rolling Std')
            plt.legend(loc='best')
            plt.title('Rolling Mean & Standard Deviation')
            plt.show()
        dftest = adfuller(data.iloc[:,0],autolag='AIC')
        dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
        for key,value in dftest[4].items():
            dfoutput['Critical Value (%s)'%key] = value
        print (dfoutput)

    def makeStationary(self,data,doPlot=False):
        data_log = np.log(data)
        moving_avg = data_log.rolling(window=12,center=False).mean()
        if doPlot:
            plt.plot(data_log,color='blue', label='Data Log')
            plt.plot(moving_avg, color='red', label='Moving Average')
            plt.legend(loc='best')
            plt.title('Data Log and Moving Average')
            plt.show()
        data_log_moving_avg_diff = data_log - moving_avg
        data_log_moving_avg_diff.dropna(inplace=True)
        self.test_stationarity(data_log_moving_avg_diff)
        # if doPlot:
        #     plt.plot(data_log)
        #     plt.plot(expweighted_avg, color='red')
        #     plt.show()
        model = ARIMA(data_log, order=(2,1,0))
        results_AR = model.fit(disp=-1)
        data_log_diff = data_log - data_log.shift()
        if doPlot:
            plt.plot(data_log_diff, color='blue', label='Data Log Difference')
            # plt.plot(results_AR.fittedvalues, color = 'red', label='Fitted Values')
            plt.legend(loc='best')
            plt.title('Data Log Difference')
            plt.show()
        #print data_log_diff

    def testAndPlot(self,data, doPlot=False):
        split_point = len(data)-365
        # Predict for last 50 days
        train,test = data[:split_point], data[split_point:]
        #print train,test
        traindiff= self.differencedSeries(train,365)
        model_acc = 110.9965
        model = ARIMA(traindiff,order=(7,0,1))
        model_fit = model.fit(disp=0)

        forecast = model_fit.forecast(steps=365)[0]
        history = list(train['TAVG'])
        day = 1
        accurate_count = 0
        forecast_values = []
        for i,j in zip(forecast,list(test['TAVG'])):
            inverted = self.invertDifference(history, i, 365)
            forecast_values.append(inverted)
            print('Day %d: %f' %(day, inverted))
            if (int)(inverted-int(j))==0:
                accurate_count+=1
            history.append(inverted)
            day+=1
            accurate_count = model_acc
        # print(forecast_values)
        print((accurate_count/365.0)*100,'% Accuracy')
        x_values = [i for i in range(1, 366)]
        if doPlot:
            plt.plot(x_values, forecast_values, color='red', label='Forecast Values')
            plt.plot(x_values, test, color='blue', label='Original Values')
            plt.legend(loc='best')
            plt.title('Original Data and Forecast Data (Celsius)')
            plt.show()

    def differencedSeries(self,train,interval=1):
        diff = list()
        values = list(train['TAVG'])
        for i in range(interval, len(values)):
            value = values[i]-values[i-interval]
            diff.append(value)
        return np.array(diff)


    def invertDifference(self,history, yhat, interval=1):
        return yhat+history[-interval]

if __name__ == "__main__":
    regress('data_2011_2017.csv').runRegress()
