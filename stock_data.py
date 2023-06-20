import yfinance as yf
import pandas_ta as ta
import numpy as np
from sklearn.preprocessing import MinMaxScaler

class stock_data:
    def __init__(self, stock_name, start_date, end_date):
        """
        Initializes the stock_data class with the stock name, start date, and end date.

        Args:
            stock_name: Name of the stock.
            start_date: Start date for retrieving stock data.
            end_date: End date for retrieving stock data.
        """
        self.name = stock_name
        self.start = start_date
        self.end = end_date
        self.data = yf.download(tickers=self.name, start=self.start, end=self.end)

    def set_start_date(self, start_date):
        """
        Sets the start date for retrieving stock data.

        Args:
            start_date: Start date for retrieving stock data.

        Returns:
            None.
        """
        self.start = start_date

    def set_end_date(self, end_date):
        """
        Sets the end date for retrieving stock data.

        Args:
            end_date: End date for retrieving stock data.

        Returns:
            None.
        """
        self.end = end_date

    def get_data(self):
        """
        Returns the downloaded stock data.

        Returns:
            Downloaded stock data.
        """
        return self.data

    def min_max_scaler(self):
        """
        Performs Min-Max scaling on the stock data.

        Returns:
            Scaled stock data.
        """
        scale = MinMaxScaler(feature_range=(0, 1))
        self.scaled_arr = scale.fit_transform(self.data)
        return self.scaled_arr

    def indicators(self):
        """
        Runs technical indicators on the stock data.
        
        Current indicators:
        Relative Strength Index
        Exponential Moving Average (Fast, Medium, and Slow Moving)

        Returns:
            None.
        """
        self.data['RSI'] = ta.rsi(self.data.Close, length=15)
        self.data['EMAF'] = ta.ema(self.data.Close, length=25)
        self.data['EMAM'] = ta.ema(self.data.Close, length=110)
        self.data['EMAS'] = ta.ema(self.data.Close, length=175)

    def filter_data(self):
        """
        Filters and preprocesses the stock data for training.

        Returns:
            Preprocessed and filtered stock data.
        """
        self.data['Next Target Close'] = self.data['Adj Close'].shift(-1)
        self.data.dropna(inplace=True)
        self.data.reset_index(inplace=True)
        self.data.drop(['Volume', 'Close', 'Date'], axis=1, inplace=True)
        return self.min_max_scaler()

    def preprocess_data(self):
        """
        Preprocesses the data to be sent to the LSTM network.

        Returns:
            True if preprocessing is successful.
        """
        self.back_candles = 10
        self.X = []

        for j in range(8):
            X_column = []
            for i in range(self.back_candles, self.scaled_arr.shape[0]):
                X_column.append(self.scaled_arr[i - self.back_candles:i, j])
            self.X.append(X_column)

        self.X = np.moveaxis(self.X, [0], [2])

        yi = np.array(self.scaled_arr[self.back_candles:, -1])
        self.y = np.reshape(yi, (len(yi), 1))

        self.X, self.y = np.array(self.X), np.array(self.y)

        return True
