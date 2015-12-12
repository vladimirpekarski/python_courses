# -*- coding: utf-8 -*-
__author__ = 'vladimir.pekarsky'

import argparse
import os
import Image


def parse_args():
    parser = argparse.ArgumentParser(description='Script to resize image files')
    parser.add_argument('-p', '--path', help='Path to folder with files')
    parser.add_argument('-r', '--remove_files',
                        help='Remove files with prefix "resized_" in specified path')

    return parser.parse_args()


def resize_images(files_dir):
    for root, dirs, files in os.walk(files_dir):
        for _file in files:
            path_to_file = os.path.join(root, _file)
            resize_image(path_to_file)


def resize_image(path_to_file):
    try:
        image = Image.open(path_to_file)
        resized_file_name = get_resized_file_name(path_to_file)
        new_image_size = image.size[0] // 2, image.size[1] // 2
        resized_image = image.resize(new_image_size)
        resized_image.save(resized_file_name, image.format)
    except IOError as e:
        print('Error {} appears for file {}'.format(e, path_to_file))


def get_resized_file_name(path_to_file):
    file_path, file_name = os.path.split(path_to_file)
    new_file_name = 'resized_' + file_name
    resized_file_path = os.path.join(file_path, new_file_name)

    return resized_file_path


def remove_created_files(files_dir):
    for root, dirs, files in os.walk(files_dir):
        for _file in files:
            if _file.startswith('resized_'):
                path_to_file = os.path.join(root, _file)
                os.remove(path_to_file)


if __name__ == '__main__':
    args = parse_args()
    if args.path:
        if os.path.exists(args.path):
            resize_images(args.path)
        else:
            print('Directory does not exist')

        print('Files have been resized')

    elif args.remove_files:
        if os.path.exists(args.remove_files):
            remove_created_files(args.remove_files)
        else:
            print('Directory does not exist')

        print('Files have been removed')
