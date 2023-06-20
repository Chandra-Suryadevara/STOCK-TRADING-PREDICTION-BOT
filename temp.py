from tkinter.font import BOLD
import customtkinter
import googlefinance as gf
import data_extractor as de
import lstm_class as ls
import lstm_class as ls
import matplotlib.pyplot as pl
import pandas as pd




    
def test():
        

aapl = de.data_extractor(entry.get().upper(), startdate = '2012-03-11', enddate = '2022-07-10')


de.data_extractor.indicators()

scaled_data = de.data_extractor.Filter_Data()

de.data_extractor.preprocess_data()

     data = de.data_extractor.get_data()

     

     lstm_train = ls.lstm_class(aapl.backcandles)

     ls.lstm_class.train(lstm_train, X_train = aapl.X, y_train = aapl.y)

     ls.lstm_class.predict(lstm_train)

     pl.figure(figsize=(16,8))
     pl.plot(aapl.y, color = 'black', label = 'Test')
     pl.plot(lstm_train.y_pred, color = 'red', label = 'Prediction')
     pl.legend()
     pl.show()

    def predict():
        stock = de.data_extractor(stock_name = (entry.get()).upper(), startdate = '2012-03-11', enddate = '2022-07-10')
        
        de.data_extractor.indicators()

        scaled_data = de.data_extractor.filter_data()
        de.data_extractor.preprocess_data()
        data = de.data_extractor.get_data()
        lstm_train = ls.lstm_class(stock.backcandles)
        ls.lstm_class.train(lstm_train, X_train = stock.X, y_train = stock.y)
        if (ls.lstm_class.get_trade_signal(ls.lstm_class.predict(lstm_train)[-1],0.5)) == 1:
          label1 = customtkinter.CTkLabel(master = frame, text = "> BUY THE STOCK", font=("Roboto" , 20, BOLD))
          label1.pack(pady =30, padx = 10)
          root.mainloop()
        else:
          label2 = customtkinter.CTkLabel(master = frame, text = "> SELL THE STOCK", font=("Roboto" , 20, BOLD))
          label2.pack(pady =30, padx = 10)
          root.mainloop()

    def ui_maker():
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        root = customtkinter.CTk()
        root.geometry("900x600")
        frame = customtkinter.CTkFrame(master = root)
        frame.pack(pady=80, padx=60, fill="both", expand = True)
        label = customtkinter.CTkLabel(master = frame, text = "STOCK PREDICTION BOT", font=("Roboto" , 30, BOLD))
        label.pack(pady =16, padx = 10)
        label3 = customtkinter.CTkLabel(master = frame, text = "PLEASE ENTER STOCK SYMBOL ", font=("Roboto" , 15, BOLD))
        label3.pack(pady =20, padx = 10)
        entry = customtkinter.CTkEntry(master = frame, placeholder_text = "STOCK NAME")
        entry.pack(pady=12,padx=10)
        button = customtkinter.CTkButton(master = frame, text = "Predict",command = PREDICT)
        button.pack(pady =12, padx = 8)
        button2 = customtkinter.CTkButton(master = frame, text = "See Accuracy",command = TEST)
        button2.pack(pady =12, padx = 14)
        root.mainloop()




if __name__ == '__main__':
  ui_maker()
    
        






