import yfinance as yf


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
