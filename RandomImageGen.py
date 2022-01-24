#!/usr/bin/env python3
# coding: utf-8

import random

import numpy as np

from PIL import ImageDraw, Image

w, h = 42, 42
#print('w, h, area: ' + str(w) + ', ' + str(h) + ', ' + str(w*h))

def image_generator(list_name, numpy_images):
    total_circles = random.randint(0, 5)
    circle_collection = []
    i = 0

    img = Image.new('L', (w,h), 'black')
    draw = ImageDraw.Draw(img)

    while i < total_circles:
        rx = random.randint(0,42)
        ry = random.randint(0,42)
        rn = random.randint(2,5)
        circle_area = []
        for n in range(rn):
            circle_area.extend([rx+n])
            circle_area.extend([ry+n])

        if (rx+n >= 42) or (ry+n >= 42):
            continue
        elif any(x in circle_area for x in circle_collection):
            continue
        elif not circle_collection:
            circle_collection.extend(circle_area)
            draw.rectangle((rx,ry,rx+rn,ry+rn), fill='white')
        else:
            circle_collection.extend(circle_area)
            draw.rectangle((rx,ry,rx+rn,ry+rn), fill='white')
        i += 1
    list_name.append(total_circles)
    img = np.array(img)
    numpy_images.append(img) #add .flatten() if needed later.
    #display(img)

acc = []
np_i = []

for i in range(10000):
    image_generator(acc, np_i)
acc = np.array(acc)
np_i = np.array(np_i)
acc

np.save('labels', acc)

np.save('images', np_i)

