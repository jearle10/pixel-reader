import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPool2D, Dropout


class ConvClassifier(tf.keras.Model):
    def __init__(self, classes, prob_drop):
        super(ConvClassifier, self).__init__()
        self.prob_drop = prob_drop
        self.classes = classes

        self.classify = tf.keras.Sequential()
        self.classify.add(Conv2D(16, 3, padding='same', activation='relu'))
        self.classify.add(MaxPool2D(2))
        self.classify.add(Conv2D(32, 3, padding='same', activation='relu'))
        self.classify.add(MaxPool2D(2))
        self.classify.add(Conv2D(64, 3, padding='same', activation='relu'))
        self.classify.add(MaxPool2D(2))
        self.classify.add(Conv2D(128, 3, padding='same', activation='relu'))
        self.classify.add(MaxPool2D(2))
        self.classify.add(Flatten())
        self.classify.add(Dense(256, activation='relu'))
        self.classify.add(Dropout(prob_drop))
        self.classify.add(Dense(128, activation='relu'))
        self.classify.add(Dropout(prob_drop))
        self.classify.add(Dense(64, activation='relu'))
        self.classify.add(Dropout(prob_drop))
        self.classify.add(Dense(classes, activation='softmax'))

    def call(self, inputs):
        return self.classify(inputs)


