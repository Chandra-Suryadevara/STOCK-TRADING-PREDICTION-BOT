from keras.models import Model
from keras.layers import LSTM, Dropout, Dense, Input, Activation
from keras import optimizers
import numpy as np

class lstm_class:
    def __init__(self, backcandles):
        self.backcandles = backcandles
        np.random.seed(10)
        self.model = self.build_model()


    def create_lstm_layer(self, inputs):
        return LSTM(150, name='first_layer')(inputs)


    def create_dense_layer(self, inputs):
        return Dense(1, name='dense_layer')(inputs)


    def create_output_layer(self, inputs):
        return Activation('linear', name='output')(inputs)


    def build_model(self):
        lstm_input = Input(shape=(self.backcandles, 8), name='lstm_input')
        inputs = self.create_lstm_layer(lstm_input)
        inputs = self.create_dense_layer(inputs)
        output = self.create_output_layer(inputs)
        model = Model(inputs=lstm_input, outputs=output)
        adam = optimizers.Adam()
        model.compile(optimizer=adam, loss='mse')
        return model

   
    def train(self, X_train, y_train, batch_size=15, epochs=30, validation_split=0.1):
        self.X_train = X_train
        self.model.fit(x=X_train, y=y_train, batch_size=batch_size, epochs=epochs, shuffle=True, validation_split=validation_split)

    def predict(self):
        self.y_pred = self.model.predict(self.X_train)
        
        return self.y_pred

    def get_trade_signal(prediction, threshold=0.5):
     if prediction >= threshold:
        return 1
     else:
        return 0


