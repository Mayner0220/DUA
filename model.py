import tensorflow as tf
from tensorflow.keras.layers import *

class Model(tf.keras.Model):
    def __init__(self):
        super(Model, self).__init__()
        self.lstm = LSTM()