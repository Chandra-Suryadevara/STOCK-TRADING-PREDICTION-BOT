import Data_Extractor as de
import LSTMCLASS as ls
import matplotlib.pyplot as pl
import pandas as pd

aapl = de.Data_Extractor(stock_name = 'AAPL', startdate = '2012-03-11', enddate = '2022-07-10')

de.Data_Extractor.Downloader(aapl)

de.Data_Extractor.Indincators(aapl)

scaled_data = de.Data_Extractor.Filter_Data(aapl)

de.Data_Extractor.preprocess_data(aapl)

data = de.Data_Extractor.get_data(aapl)

print(data.head(10))

lstm_train = ls.LSTMCLASS(aapl.backcandles)

ls.LSTMCLASS.train(lstm_train, X_train = aapl.X, y_train = aapl.y)

ls.LSTMCLASS.predict(lstm_train)

pl.figure(figsize=(16,8))
pl.plot(aapl.y, color = 'black', label = 'Test')
pl.plot(lstm_train.y_pred, color = 'red', label = 'Prediction')
pl.legend()
pl.show()