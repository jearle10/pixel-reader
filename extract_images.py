import cv2
import pandas as pd
import os

PATH = '/mnt/d/projects/cards_project/pixel-reader/data'
TRAIN_FOLDER_SAVE = 'train_images'
TEST_FOLDER_SAVE = 'test_images'

if __name__ == '__main__':
    # read files
    path_train = os.path.join(PATH, 'train_zipped')
    path_test = os.path.join(PATH, 'test_zipped')
    train = pd.read_csv(os.path.join(PATH, 'train_cards_label.csv'))
    test = pd.read_csv(os.path.join(PATH, 'test_cards_label.csv'))
    # unique filenames
    train_filenames = train['filename'].unique().tolist()
    test_filenames = test['filename'].unique().tolist()
    # loop over  train images
    for filename in train_filenames:
        sub_df = train[train['filename'] == filename]
        image_path = os.path.join(path_train, filename)
        image = cv2.imread(image_path)
        # loop over examples in image
        for index, row in sub_df.iterrows():
            x_min = row['xmin']
            x_max = row['xmax']
            y_min = row['ymin']
            y_max = row['ymax']
            label = row['label']
            label_str = row['class']

            sub_image = image[y_min:y_max, x_min:x_max]
            save_name = '{}/{}/{}_{}_{}.jpg'.format(PATH, TRAIN_FOLDER_SAVE,
                                                    filename[:-4], label, label_str)
            cv2.imwrite(save_name, sub_image)
    # loop over test images
    for filename in test_filenames:
        sub_df = test[test['filename'] == filename]
        image_path = os.path.join(path_test, filename)
        image = cv2.imread(image_path)
        # loop over examples in image
        for index, row in sub_df.iterrows():
            x_min = row['xmin']
            x_max = row['xmax']
            y_min = row['ymin']
            y_max = row['ymax']
            label = row['label']
            label_str = row['class']

            sub_image = image[y_min:y_max, x_min:x_max]
            save_name = '{}/{}/{}_{}_{}.jpg'.format(PATH, TEST_FOLDER_SAVE,
                                                    filename[:-4], label, label_str)
            cv2.imwrite(save_name, sub_image)

