from lstm_class import lstm_class
import unittest


class TestLSTMClass(unittest.TestCase):
    def setUp(self):
        self.backcandles = 10
        self.lstm = lstm_class(self.backcandles)

    def test_get_trade_signal(self):
        prediction = 0.6
        signal = self.lstm.get_trade_signal(prediction, threshold=0.5)
        self.assertEqual(signal, 1)

        prediction = 0.4
        signal = self.lstm.get_trade_signal(prediction, threshold=0.5)
        self.assertEqual(signal, 0)

if __name__ == '__main__':
    unittest.main()
