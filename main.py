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
        self.mainloop()

    def predict(self):
        # Setup Stock
        self.update()
        ticker = yf.Ticker(self.entry.get().upper())
        try:
            check = ticker.info
        except Exception as e:
            self.label5 = customtkinter.CTkLabel(master=self.frame,
                                                 text="Please Enter the Correct Stock Ticker",
                                                 font=("Roboto", 20, BOLD))
            self.label5.pack(pady=30, padx=10)
            self.update()
            # sleep for 5 seconds
            time.sleep(5)
            self.label5.destroy()
            return
        self.label5 = customtkinter.CTkLabel(master=self.frame,
                                             text="Training the prediction on your stock...",
                                             font=("Roboto", 20, BOLD))
        self.label5.pack(pady=30, padx=10)
        self.update()

        self.label1 = customtkinter.CTkLabel(master=self.frame, text="BUY THE STOCK", font=("Roboto", 20, BOLD))

        self.stock = sd.stock_data(self.entry.get().upper(), '2012-03-11', '2022-07-10')
        self.stock.indicators()
        self.stock.filter_data()
        self.stock.preprocess_data()

        self.model = ls.lstm_class(self.stock.back_candles)
        self.model.train(self.stock.X, self.stock.y)

        if self.model.get_trade_signal(self.model.predict()[-1], 0.5) == 1:
            self.label5.destroy()
            self.label1.destroy()
            self.label1 = customtkinter.CTkLabel(master=self.frame, text="BUY THE STOCK", font=("Roboto", 20, BOLD))
            self.label1.pack(pady=30, padx=10)
            self.update()
        else:
            self.label5.destroy()
            self.label1.destroy()
            self.label1 = customtkinter.CTkLabel(master=self.frame, text="SELL THE STOCK", font=("Roboto", 20, BOLD))
            self.label1.pack(pady=30, padx=10)
            self.update()

    def visualize(self):
        # checks if prediction has been made.
        try:
            try_predict = self.model
        except Exception as e:
            self.label1 = customtkinter.CTkLabel(master=self.frame,
                                                 text="Please predict before visualizing.",
                                                 font=("Roboto", 20, BOLD))
            self.label1.pack(pady=30, padx=10)
            self.update()
            time.sleep(5)
            self.label1.destroy()
            return
        # plot data
        pl.figure(figsize=(16, 8))
        pl.plot(self.stock.y, color='black', label='Test')
        pl.plot(self.model.y_pred, color='red', label='Prediction')
        pl.legend()
        pl.show()

if __name__ == '__main__':
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    root = root()
    root.mainloop()
