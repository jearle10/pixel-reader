import tensorflow as tf
import numpy as np
import os
import cv2
from utils import class_int_to_text
from model import ConvClassifier
import config

MODEL_PATH = '/mnt/d/projects/cards_project/pixel-reader/models/model_weights'
TEST_FOLDER_LOCATION = '/mnt/d/projects/cards_project/pixel-reader/models/test_images'
TEST_FILE_NAME = '003212838_1_7s.jpg'

MODEL_CHECKPOINT = 'test_model'
MODEL_FILE = os.path.join(MODEL_PATH, MODEL_CHECKPOINT)

IMAGE_HEIGHT = 80
IMAGE_WIDTH = 80


def prepare_image(image):
    height, width = image.shape[:2]
    if height != IMAGE_HEIGHT or width != IMAGE_WIDTH:
        image = cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
    image = image / 255.
    return image


def load_image(image_location):
    return cv2.imread(image_location)


def predict_card_type(image_location):
    model = ConvClassifier(config.NO_CARDS, 0)
    model.load_weights(MODEL_FILE)

    image = load_image(image_location)
    image = prepare_image(image)
    image = tf.expand_dims(image, axis=0)

    pred = model.predict(image)
    pred = np.argmax(pred, axis=-1)[0]
    pred += 1
    pred_string = class_int_to_text(pred)
    return pred_string

#
#
#
# if __name__ == '__main__':
#     image_location = os.path.join(TEST_FOLDER_LOCATION, TEST_FILE_NAME)
#     card_type = predict_card_type(image_location)
#     print(card_type)
