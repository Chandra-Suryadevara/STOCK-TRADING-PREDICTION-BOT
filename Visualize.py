import Data_Extractor as de
import matplotlib.pyplot as pl
import pandas as pd

aapl = de.Data_Extractor(stock_name = 'AAPL', startdate = '2012-03-11', enddate = '2022-07-10')

de.Data_Extractor.Downloader(aapl)

data = de.Data_Extractor.get_data(aapl)

print(data.head(10))


