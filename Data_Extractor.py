import yfinance as yf
import pandas_ta as ta
import numpy as np

from sklearn.preprocessing import MinMaxScaler
# Data Extractor Class
# Takes a Stock, Start date and End Date.

class Data_Extractor:
    
    def __init__(self,stock_name,startdate,enddate):
        self.name = stock_name
        self.start = startdate
        self.end = enddate

    # Download stock data from yfinance
    def Downloader(self):
        self.Data = yf.download(tickers = self.name, start = self.start,end=self.end)
    
    
    def set_start_date(self, start_date):
        self.start = start_date

    def set_end_date(self, end_date):
       self.end = end_date
        
    def get_data(self):
        return self.Data


    #Data Scaler using mix max scaling
    def min_max_scaler(self):
     scale = MinMaxScaler(feature_range=(0,1))
     self.scaled_arr = scale.fit_transform(self.Data)
     return self.scaled_arr

    #Runs Technical indicators on the data provided
    def Indincators(self):
        #Relative Strength Index Indicator
        self.Data['RSI'] = ta.rsi(self.Data.Close, length = 15)
        #Exponetial Moving Average Indicator
        
        #Fast Moving Average
        self.Data['EMAF'] = ta.ema(self.Data.Close,length = 25)
        #Medium Moving Average
        self.Data['EMAM'] = ta.ema(self.Data.Close,length = 110)
        #Slow Moving Average
        self.Data['EMAS'] = ta.ema(self.Data.Close,length = 175)
    
    #Drop unwated data columns
    def Filter_Data(self):
        self.Data['Next Target Close'] = self.Data['Adj Close'].shift(-1)
        self.Data.dropna(inplace=True)
        self.Data.reset_index(inplace = True)
        self.Data.drop(['Volume', 'Close','Date'],axis = 1,inplace = True)
        return self.min_max_scaler()

    #Prepoccess Data to be sent to the LSTM network.
    def preprocess_data(self):
      self.backcandles=10
      self.X = []

      for j in range(8):
        X_column = []

        for i in range(self.backcandles, self.scaled_arr.shape[0]):
            X_column.append(self.scaled_arr[i - self.backcandles:i, j])

        self.X.append(X_column)

      self.X = np.moveaxis(self.X, [0], [2])

      yi = np.array(self.scaled_arr[self.backcandles:, -1])
      self.y = np.reshape(yi, (len(yi), 1))

      self.X, self.y = np.array(self.X), np.array(self.y)

      return True