import tensorflow as tf
from model import ConvClassifier
import os
import pathlib

NO_CARDS = 52
DATA_PATH = '/mnt/d/projects/cards_project/pixel-reader/data'
TRAIN_IMAGES = 'train_images'
TEST_IMAGES = 'test_images'

BATCH_SIZE = 256
EPOCHS = 50
CLASSES = [str(i).zfill(2) for i in range(1, NO_CARDS+1)]
PROB_DROP = 0.25
AUGMENT = True


def get_label(path):
    label = tf.strings.split(path, '_')[-2]
    return label == CLASSES


def decode_img(img):
    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    return img


def process_path(path):
    label = get_label(path)
    img = tf.io.read_file(path)
    img = decode_img(img)
    return img, label


if __name__ == '__main__':
    train_files_root = pathlib.Path(os.path.join(DATA_PATH, TRAIN_IMAGES))
    test_files_root = pathlib.Path(os.path.join(DATA_PATH, TEST_IMAGES))

    data_augmentation = tf.keras.Sequential([
        tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
        tf.keras.layers.experimental.preprocessing.RandomRotation(0.2),
    ])

    train_dataset = tf.data.Dataset.list_files(str(train_files_root/'*'))
    train_dataset = train_dataset.map(process_path)
    train_dataset = train_dataset.padded_batch(BATCH_SIZE, padded_shapes=([80, 80, 3], [None]))
    if AUGMENT:
        train_dataset = train_dataset.map(lambda x, y: (data_augmentation(x, training=True), y))

    test_dataset = tf.data.Dataset.list_files(str(test_files_root / '*'))
    test_dataset = test_dataset.map(process_path)
    test_dataset = test_dataset.padded_batch(BATCH_SIZE, padded_shapes=([80, 80, 3], [None]))
    if AUGMENT:
        test_dataset = test_dataset.map(lambda x, y: (data_augmentation(x, training=True), y))

    classifier = ConvClassifier(classes=NO_CARDS, prob_drop=PROB_DROP)
    classifier.compile(optimizer='adam', loss=tf.keras.losses.CategoricalCrossentropy(), metrics=['accuracy'])
    classifier.fit(train_dataset, epochs=EPOCHS, validation_data=test_dataset)

    classifier.save("model_file")