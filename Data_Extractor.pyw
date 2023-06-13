import yfinance as yf
import pandas_ta as ta
import numpy as np


class Data_Extractor:
    
    def __init__(self,stock_name,startdate,enddate):
        self.name = stock_name
        self.start = startdate
        self.end = enddate

    def Downloader(self):
        self.Data = yf.download(tickers = self.name, start = self.start,end=self.end)
    
    def update_Dates(self,startdate,enddate):
        self.start=startdate
        self.end=enddate

    def get_data(self):
        return self.Data

    def min_max_scaler(self):
     
     min_val = min([min(row) for row in self.Data])
     max_val = max([max(row) for row in self.Data])
     self.scaled_arr = [[(val - min_val) / (max_val - min_val) for val in row] for row in self.Data]
     return self.scaled_arr

    def Indincators(self):
        self.Data['RSI'] = ta.rsi(self.Data.Close, length = 15)
        self.Data['EMAF'] = ta.ema(self.Data.Close,length = 20)
        self.Data['EMAM'] = ta.ema(self.Data.Close,length = 100)
        self.Data['EMAS'] = ta.ema(self.Data.Close,length = 150)

    def Filter_Data(self):
        self.Data['Next Target Close'] = self.Data['Adj Close'].shift(-1)
        self.Data.dropna(inplace=True)
        self.Data.reset_index(inplace = True)
        self.Data.drop(['Volume', 'Close','Date'],axis = 1,inplace = True)
        return self.min_max_scaler(self.Data)

    def preprocess_data(self):
      backcandles=30
      self.X = []

      for j in range(8):
        X_column = []

        for i in range(backcandles, self.scaled_arr.shape[0]):
            X_column.append(self.scaled_arr[i - backcandles:i, j])

        self.X.append(X_column)

      self.X = np.moveaxis(self.X, [0], [2])

      yi = np.array(self.scaled_arr[backcandles:, -1])
      self.y = np.reshape(yi, (len(yi), 1))

      self.X, self.y = np.array(self.X), np.array(self.y)

      return True