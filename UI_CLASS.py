from tkinter.font import BOLD
import customtkinter
import googlefinance as gf
import Data_Extractor as de
import LSTMCLASS as ls



class UI_CLASS:
    
    

    def PREDICT(self):
        stock = de.Data_Extractor(stock_name = (self.entry.get()).upper(), startdate = '2012-03-11', enddate = '2022-07-10')
        de.Data_Extractor.Downloader(stock)
        de.Data_Extractor.Indincators(stock)
        scaled_data = de.Data_Extractor.Filter_Data(stock)
        de.Data_Extractor.preprocess_data(stock)
        data = de.Data_Extractor.get_data(stock)
        lstm_train = ls.LSTMCLASS(stock.backcandles)
        ls.LSTMCLASS.train(lstm_train, X_train = stock.X, y_train = stock.y)
        ls.LSTMCLASS.predict(lstm_train)

    def UI_MAKER(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.root = customtkinter.CTk()
        self.root.geometry("900x600")
        self.frame = customtkinter.CTkFrame(master = self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand = True)
        self.label = customtkinter.CTkLabel(master = self.frame, text = "STOCK PREDICTION BOT", font=("Roboto" , 30, BOLD))
        self.label.pack(pady =16, padx = 10)
        self.entry = customtkinter.CTkEntry(master = self.frame, placeholder_text = "STOCK NAME")
        self.entry.pack(pady=12,padx=10)
        self.button = customtkinter.CTkButton(master = self.frame, text = "Predict",command = self.PREDICT)
        self.button.pack(pady =12, padx = 10)
        self.root.mainloop()

    def __init__(self):
        self.UI_MAKER()
    
        






