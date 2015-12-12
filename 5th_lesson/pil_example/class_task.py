# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import Image
import ImageEnhance
import os


def image_manipulate(image_url):
    file_path, file_name = os.path.split(image_url)
    rotated_file_name = 'rotated_' + file_name
    resized_file_name = 'resized_' + file_name
    contrasted_file_name = 'contrasted' + file_name
    rotated_file_path = os.path.join(file_path, rotated_file_name)
    resized_file_path = os.path.join(file_path, resized_file_name)
    contrasted_file_path = os.path.join(file_path, contrasted_file_name)

    try:
        image = Image.open(image_url)
        print('Image type: {}'.format(image.format))
        enh = ImageEnhance.Contrast(image)
        contrasted_image = enh.enhance(1.5)

        image_size = image.size
        doubled_size = double_size(image_size)
        resized_image = image.resize(doubled_size)
        rotated_image = image.rotate(45)

        rotated_image.save(rotated_file_path, image.format)
        resized_image.save(resized_file_path, image.format)
        contrasted_image.save(contrasted_file_path, image.format)
    except IOError as e:
        print('Can\'t manipulate with image: {}'.format(e))


def double_size(origin_sizes):
    size_list = list(origin_sizes)
    for index, size in enumerate(size_list):
        size_list[index] = size * 2

    return tuple(size_list)

