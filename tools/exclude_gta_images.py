import argparse

import os

parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')
                    

parser.add_argument('-d', '--dir', default='data/gta')


args = parser.parse_args()

dir_path = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(dir_path, 'gta_exclude.txt')) as f:
    lines = [line.strip() for line in f.readlines()]


# image_dir = os.path.join(os.path.dirname(dir_path), 'data/gta/images')
# label_dir = os.path.join(os.path.dirname(dir_path), 'data/gta/labels')
image_dir = args.dir + '/images'
label_dir = args.dir + '/labels'

print(image_dir)
print(label_dir)

train_label_counter = 0
label_counter = 0
image_counter = 0
for i, img in enumerate(lines):

    img_path = os.path.join(image_dir, img)
    if os.path.exists(img_path):
        image_counter += 1
        os.remove(img_path)

    label_path = os.path.join(label_dir, img)
    if os.path.exists(label_path):
        label_counter += 1
        os.remove(label_path)

    train_label = os.path.join(label_dir, img.split('.')[0] + '_labelTrainIds.png')
    if os.path.exists(train_label):
        train_label_counter += 1
        os.remove(train_label)

print('removed', image_counter, 'images')
print('removed', label_counter, 'labels')
print('removed', train_label_counter, 'train labels')
