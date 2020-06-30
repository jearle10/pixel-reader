import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPool2D


class ConvClassifier(tf.keras.Model):
    def __init__(self, classes):
        super(ConvClassifier, self).__init__()
        self.conv_layers = tf.keras.Sequential()
        self.conv_layers.add(Conv2D(32, (5, 5), padding='same', activation='relu'))
        self.conv_layers.add(MaxPool2D((2, 2)))
        self.conv_layers.add(Conv2D(64, (5, 5), padding='same', activation='relu'))
        self.conv_layers.add(MaxPool2D((2, 2)))
        self.conv_layers.add(Conv2D(128, (5, 5), padding='same', activation='relu'))
        self.conv_layers.add(MaxPool2D((2, 2)))

        self.classify = tf.keras.Sequential()
        self.classify.add(Flatten())
        self.classify.add(Dense(512, activation='relu'))
        self.classify.add(Dense(classes, activation='softmax'))

    def call(self, inputs):
        x = self.conv_layers(inputs)
        return self.classify(x)
