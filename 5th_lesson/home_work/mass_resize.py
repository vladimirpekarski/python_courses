# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import os
import Image

path = r'files'

def resize_images_in_folder(files_dir):
    if os.path.exists(files_dir):
        resize_images(files_dir)
    else:
        print('Directory does not exist')


def resize_images(files_dir):
    for root, dirs, files in os.walk(files_dir):
        for file in files:
            path_to_file = os.path.join(root, file)
            resize_image(path_to_file)


def resize_image(path_to_file):
    try:
        image = Image.open(path_to_file)
        resized_file_name = get_resized_file_name(path_to_file)
        new_image_size = reduce_size(image.size)
        resized_image = image.resize(new_image_size)
        resized_image.save(resized_file_name, image.format)
    except IOError as e:
        print('Error {} appears for file {}'.format(e, path_to_file))


def get_resized_file_name(path_to_file):
    file_path, file_name = os.path.split(path_to_file)
    new_file_name = 'resized_' + file_name
    resized_file_path = os.path.join(file_path, new_file_name)

    return resized_file_path


def reduce_size(origin_sizes):
    size_list = list(origin_sizes)
    for index, size in enumerate(size_list):
        size_list[index] = size // 2

    return tuple(size_list)


def remove_created_files(files_dir):
    for root, dirs, files in os.walk(files_dir):
        for file in files:
            if file.startswith('resized_'):
                path_to_file = os.path.join(root, file)
                os.remove(path_to_file)



resize_images_in_folder(path)

# Delete all files with prefix 'resized_' in specified folder
# remove_created_files(path)
