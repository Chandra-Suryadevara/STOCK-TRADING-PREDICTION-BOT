import Data_Extractor as de
import LSTMCLASS as ls
import matplotlib.pyplot as pl
import pandas as pd

aapl = de.Data_Extractor(stock_name = 'AAPL', startdate = '2012-03-11', enddate = '2022-07-10')

de.Data_Extractor.Downloader(aapl)

de.Data_Extractor.Indincators(aapl)

scaled_data = de.Data_Extractor.Filter_Data(aapl)

de.Data_Extractor.preprocess_data(aapl)

# print(aapl.X)
# print(aapl.y)

data = de.Data_Extractor.get_data(aapl)

print(data.head(10))




