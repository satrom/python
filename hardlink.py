# coding: utf-8

import os
import argparse
import time

'''
创建硬链接

不能跨盘创建硬链接

请认真确认信息
请认真确认信息
请认真确认信息


使用方法:
    python hardlink.py -s 源路径 -d 目标路径
'''

is_dir = os.path.isdir
is_file = os.path.isfile
is_link = os.path.islink
join = os.path.join
abspath = os.path.abspath
exists = os.path.exists
splitext = os.path.splitext

def mkdir(path):
    if not exists(path):
        os.mkdir(path)

def mklink(src, desc):
    if not exists(desc):
        os.link(src, desc)

def hardlink(src_path, desc_path):
    abs_src_path = abspath(src_path)
    abs_desc_path = abspath(desc_path)
    if is_file(abs_src_path):
        os.link(abs_src_path, abs_desc_path)
    mkdir(abs_desc_path)
    dir_or_file_list = os.listdir(src_path)
    for dir_or_file in dir_or_file_list:
        if dir_or_file == "@eaDir":
            continue
        dir_or_file_path = join(abs_src_path, dir_or_file)
        desc_dir_or_file_path = join(abs_desc_path, dir_or_file)
        if is_file(dir_or_file_path):
            suffix = splitext(dir_or_file_path)[-1]
            if suffix in [".nfo"]:
                continue
            if os.path.basename(dir_or_file_path) in ["banner.jpg", "clearart.png", "clearlogo.png", "disc.png", "fanart.jpg", "keyart.jpg", "logo.png", "poster.jpg", "thumb.jpg"]:
                continue
            print("创建硬链接: {} to {}".format(dir_or_file_path, desc_dir_or_file_path))
            mklink(dir_or_file_path, desc_dir_or_file_path)
        elif is_dir(dir_or_file_path):
            print("创建目录: {}".format(dir_or_file_path))
            mkdir(desc_dir_or_file_path)
            hardlink(dir_or_file_path, desc_dir_or_file_path)
