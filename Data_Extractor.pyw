import yfinance as yf
import pandas_ta as ta


class Data_Extractor:
    
    def __init__(self,stock_name,startdate,enddate):
        self.name = stock_name
        self.start = startdate
        self.end = enddate

    def Downloader(self):
        self.Data = yf.download(tickers = self.stock_name, start = self.start,end=self.end)
    
    def update_Dates(self,startdate,enddate):
        self.start=startdate
        self.end=enddate

    def get_data(self):
        return self.Data

    def min_max_scaler(data):
     min_val = min(data)
     max_val = max(data)
    
     scaled_data = []
     for value in data:
        scaled_value = (value - min_val) / (max_val - min_val)
        scaled_data.append(scaled_value)
    
     return scaled_data

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

    
