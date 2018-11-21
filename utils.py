# ----------------------------------------------------------
#
# Project name: DMCRID-MulCAM-reID
# File name: utils.py
#
# Last modified: 2018-11-21
#
# ----------------------------------------------------------


# Import the necessary packages
import os

from shutil import copyfile


# Helper functions

def split_subfolder(base_path, folder_name, save_path, save_folder_name):
    folder_path = os.path.join(base_path, folder_name)
    saved_folder_path = os.path.join(save_path, save_folder_name)

    if not os.path.exists(saved_folder_path):
        os.makedirs(saved_folder_path)

    for root, dirs, files in os.walk(folder_path, topdown=True):
        for name in files:
            if not name[-3:] == 'jpg':
                continue
            ID = name.split('_')
            src_path = folder_path + '/' + name
            dst_path = saved_folder_path + '/' + ID[0]

            if not os.path.exists(dst_path):
                os.makedirs(dst_path)

            copyfile(src_path, dst_path + '/' + name)


def split_train_val(base_path, folder_name, save_path, train_name, val_name):
    folder_path = os.path.join(base_path, folder_name)
    train_path = os.path.join(save_path, train_name)
    val_path = os.path.join(save_path, val_name)

    if not os.path.exists(train_path):
        os.makedirs(train_path)
        os.makedirs(val_path)

    for root, dirs, files in os.walk(folder_path, topdown=True):
        for name in files:
            if not name[-3:] == 'jpg':
                continue
            ID = name.split('_')
            src_path = folder_path + '/' + name
            dst_path = train_path + '/' + ID[0]

            if not os.path.exists(dst_path):
                os.makedirs(dst_path)
                # The first image is used as val image
                dst_path = val_path + '/' + ID[0]
                os.makedirs(dst_path)

            copyfile(src_path, dst_path + '/' + name)


# -------------------------------------------------------------------
# Test split_subfolder
# -------------------------------------------------------------------
if __name__ == '__main__':
    download_path = './datasets/Market-1501'
    if not os.path.exists(download_path):
        print('[!] please change the download_path')

    save_path = os.path.join(download_path, 'demo')
    print(save_path)
    # ./datasets/Market-1501/demo


    if not os.path.exists(save_path):
        os.makedirs(save_path)

    split_subfolder(download_path, 'query', save_path, 'query')