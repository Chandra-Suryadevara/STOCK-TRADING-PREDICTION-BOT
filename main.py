from tkinter.font import BOLD
import customtkinter as customtkinter
import stock_data as sd
import lstm_class as ls
import matplotlib.pyplot as pl
import yfinance as yf
import time

class root(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")
        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(pady=80, padx=60, fill="both", expand=True)
        self.label = customtkinter.CTkLabel(master=self.frame, text="STOCK PREDICTION BOT", font=("Roboto", 30, BOLD))
        self.label.pack(pady=16, padx=10)
        self.label3 = customtkinter.CTkLabel(master=self.frame, text="PLEASE ENTER STOCK SYMBOL ", font=("Roboto", 15, BOLD))
        self.label3.pack(pady=20, padx=10)
        self.entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="STOCK NAME")
        self.entry.pack(pady=12, padx=10)
        self.button = customtkinter.CTkButton(master=self.frame, text="Predict", command=self.predict)
        self.button.pack(pady=12, padx=8)
        self.button2 = customtkinter.CTkButton(master=self.frame, text="See Accuracy", command=self.visualize)
        self.button2.pack(pady=12, padx=14)
        self.label5 = customtkinter.CTkLabel(master=self.frame,
                                                 text="",
                                                 font=("Roboto", 20, BOLD))
        self.label5.pack(pady=30, padx=10)

    def predict(self):        
        #Check if stock ticker exists
        ticker = yf.Ticker(self.entry.get().upper())
        try:
            check = ticker.info
        except Exception as e:
            self.label5.configure(text = "Please enter the correct Stock Ticker.")
            return
        
        # Setup Stock
        self.stock = sd.stock_data(self.entry.get().upper(), '2012-03-11', '2022-07-10')
        self.stock.indicators()
        #Check if stock has data for time-frame.
        try:
          self.stock.filter_data()
        except Exception as e:
          self.label5.configure(text = "No price data found, symbol may be delisted")
          return 
        
        self.stock.preprocess_data()
        self.model = ls.lstm_class(self.stock.back_candles)
        self.label5.configure(text = "Training the prediction on your stock...")
        self.update()
        self.model.train(self.stock.X, self.stock.y)
        

        if self.model.get_trade_signal(self.model.predict()[-1], 0.5) == 1:
            self.label5.configure(text = "BUY THE STOCK")
        else:
            self.label5.configure(text = "SELL THE STOCK")

    def visualize(self):
        # checks if prediction has been made.
        try:
            try_predict = self.model
        except Exception as e:
            self.label5.configure(text = "Please predict before visualizing")
            self.update()
            time.sleep(5)
            self.label5.configure(text = "")
            return
        # plot data
        pl.figure(figsize=(16, 8))
        pl.plot(self.stock.y, color='black', label='Test')
        pl.plot(self.model.y_pred, color='red', label='Prediction')
        pl.legend()
        pl.show()

if __name__ == '__main__':
    #Set theme of tkinter
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    #Start application
    root = root()
    root.mainloop()
