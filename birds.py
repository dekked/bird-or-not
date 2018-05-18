#!/usr/bin/env python3
"""
Solver for https://xkcd.com/1425/ in a few lines of Keras code, leveraging
ResNet-50 pre-trained on ImageNet (no further finetuning).

Usage:
    Put your images in `images` folder and run:

        python birds.py images

    The program will print which photos are of birds and which ones are not.
"""
import os
import sys

import numpy as np

from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from keras.preprocessing.image import load_img, img_to_array
from nltk.corpus import wordnet as wn


def synset_is_bird(synset):
    if synset.name() == 'bird.n.01':
        return True
    return any(synset_is_bird(ss) for ss in synset.hypernyms())


def is_bird(model, img_path):
    # Load image and transform for model input
    x = load_img(img_path, target_size=(224, 224))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Run image through network and decode result
    preds = model.predict(x)
    top_pred = decode_predictions(preds, top=1)[0][0]  # (offset_id, name, prob)

    return synset_is_bird(wn.of2ss(top_pred[0][1:] + top_pred[0][0]))


if __name__ == '__main__':
    images_dir = sys.argv[1]
    model = ResNet50()  # Initialize pre-trained model (ImageNet)

    for fname in os.listdir(images_dir):
        path = os.path.join(images_dir, fname)
        print(fname, '-', 'Bird!' if is_bird(model, path) else 'NOT bird')
