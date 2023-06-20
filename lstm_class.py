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
        """
        Creates an LSTM layer with 150 units.

        Args:
            inputs: Input tensor to the LSTM layer.

        Returns:
            LSTM layer.
        """
        return LSTM(150, name='first_layer')(inputs)

    def create_dense_layer(self, inputs):
        """
        Creates a dense layer with 1 unit.

        Args:
            inputs: Input tensor to the dense layer.

        Returns:
            Dense layer.
        """
        return Dense(1, name='dense_layer')(inputs)

    def create_output_layer(self, inputs):
        """
        Creates an output layer with linear activation.

        Args:
            inputs: Input tensor to the output layer.

        Returns:
            Output layer.
        """
        return Activation('linear', name='output')(inputs)

    def build_model(self):
        """
        Builds the LSTM model.

        Returns:
            Compiled LSTM model.
        """
        lstm_input = Input(shape=(self.backcandles, 8), name='lstm_input')
        inputs = self.create_lstm_layer(lstm_input)
        inputs = self.create_dense_layer(inputs)
        output = self.create_output_layer(inputs)
        model = Model(inputs=lstm_input, outputs=output)
        adam = optimizers.Adam()
        model.compile(optimizer=adam, loss='mse')
        return model

    def train(self, X_train, y_train, batch_size=15, epochs=30, validation_split=0.1):
        """
        Trains the LSTM model.

        Args:
            X_train: Training data (input sequences).
            y_train: Target data.
            batch_size: Number of samples per gradient update.
            epochs: Number of epochs to train the model.
            validation_split: Fraction of training data to be used for validation.

        Returns:
            None.
        """
        self.X_train = X_train
        self.model.fit(x=X_train, y=y_train, batch_size=batch_size, epochs=epochs, shuffle=True, validation_split=validation_split)

    def predict(self):
        """
        Performs predictions using the trained model.

        Returns:
            Predicted values.
        """
        self.y_pred = self.model.predict(self.X_train)
        return self.y_pred

    def get_trade_signal(self, prediction, threshold=0.5):
        """
        Determines the trade signal based on the predicted value and a threshold.

        Args:
            prediction: Predicted value.
            threshold: Threshold value for classifying the trade signal.

        Returns:
            Trade signal (1 for buy, 0 for sell).
        """
        if prediction >= threshold:
            return 1
        else:
            return 0
