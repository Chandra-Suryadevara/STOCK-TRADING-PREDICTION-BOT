
from keras.models import Model
from keras.layers import LSTM, Dropout, Dense, Input, Activation
from keras import optimizers
import numpy as np

class LSTMCLASS:
    def __init__(self, backcandles):
        self.backcandles = backcandles
        np.random.seed(10)
        self.model = self.build_model()


    def createlstmlayer(self, inputs):
        return LSTM(150, name='first_layer')(inputs)


    def createdenselayer(self, inputs):
        return Dense(1, name='dense_layer')(inputs)


    def createoutputlayer(self, inputs):
        return Activation('linear', name='output')(inputs)


    def build_model(self):
        lstm_input = Input(shape=(self.backcandles, 8), name='lstm_input')
        inputs = self.createlstmlayer(lstm_input)
        inputs = self.createdenselayer(inputs)
        output = self.createoutputlayer(inputs)
        model = Model(inputs=lstm_input, outputs=output)
        adam = optimizers.Adam()
        model.compile(optimizer=adam, loss='mse')
        return model

   
    def train(self, X_train, y_train, batch_size=15, epochs=30, validation_split=0.1):
        self.model.fit(x=X_train, y=y_train, batch_size=batch_size, epochs=epochs, shuffle=True, validation_split=validation_split)
    
    def predict():
        

