from tkinter.font import BOLD
import customtkinter
import googlefinance as gf
import data_extractor as de
import LSTMCLASS as ls
import data_extractor as de
import LSTMCLASS as ls
import matplotlib.pyplot as pl
import pandas as pd



class UI_CLASS:
    
    def TEST(self):
        

     aapl = de.data_extractor(self.entry.get().upper(), startdate = '2012-03-11', enddate = '2022-07-10')


     de.data_extractor.indicators()

     scaled_data = de.data_extractor.Filter_Data()

     de.data_extractor.preprocess_data()

     data = de.data_extractor.get_data()

     

     lstm_train = ls.LSTMCLASS(aapl.backcandles)

     ls.LSTMCLASS.train(lstm_train, X_train = aapl.X, y_train = aapl.y)

     ls.LSTMCLASS.predict(lstm_train)

     pl.figure(figsize=(16,8))
     pl.plot(aapl.y, color = 'black', label = 'Test')
     pl.plot(lstm_train.y_pred, color = 'red', label = 'Prediction')
     pl.legend()
     pl.show()

    def PREDICT(self):
        stock = de.data_extractor(stock_name = (self.entry.get()).upper(), startdate = '2012-03-11', enddate = '2022-07-10')
        
        de.data_extractor.indicators()

        scaled_data = de.data_extractor.filter_data()
        de.data_extractor.preprocess_data()
        data = de.data_extractor.get_data()
        lstm_train = ls.LSTMCLASS(stock.backcandles)
        ls.LSTMCLASS.train(lstm_train, X_train = stock.X, y_train = stock.y)
        if (ls.LSTMCLASS.get_trade_signal(ls.LSTMCLASS.predict(lstm_train)[-1],0.5)) == 1:
          self.label1 = customtkinter.CTkLabel(master = self.frame, text = "> BUY THE STOCK", font=("Roboto" , 20, BOLD))
          self.label1.pack(pady =30, padx = 10)
          self.root.mainloop()
        else:
          self.label2 = customtkinter.CTkLabel(master = self.frame, text = "> SELL THE STOCK", font=("Roboto" , 20, BOLD))
          self.label2.pack(pady =30, padx = 10)
          self.root.mainloop()

    def UI_MAKER(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.root = customtkinter.CTk()
        self.root.geometry("900x600")
        self.frame = customtkinter.CTkFrame(master = self.root)
        self.frame.pack(pady=80, padx=60, fill="both", expand = True)
        self.label = customtkinter.CTkLabel(master = self.frame, text = "STOCK PREDICTION BOT", font=("Roboto" , 30, BOLD))
        self.label.pack(pady =16, padx = 10)
        self.label3 = customtkinter.CTkLabel(master = self.frame, text = "PLEASE ENTER STOCK SYMBOL ", font=("Roboto" , 15, BOLD))
        self.label3.pack(pady =20, padx = 10)
        self.entry = customtkinter.CTkEntry(master = self.frame, placeholder_text = "STOCK NAME")
        self.entry.pack(pady=12,padx=10)
        self.button = customtkinter.CTkButton(master = self.frame, text = "Predict",command = self.PREDICT)
        self.button.pack(pady =12, padx = 8)
        self.button2 = customtkinter.CTkButton(master = self.frame, text = "See Accuracy",command = self.TEST)
        self.button2.pack(pady =12, padx = 14)
        self.root.mainloop()

    def __init__(self):
        self.UI_MAKER()
    
        






