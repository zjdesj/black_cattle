#!/usr/bin/env python3
import os
import shutil
import random

print(random.__file__)


def moveFile(fileDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)
    print(filenumber, pathDir)
    rate = 0.2  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    picknumber = int(filenumber*rate)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, 13)
    for name in sample:
        label = name.replace('.jpeg', '.txt')
        shutil.move(fileDir+name, tarDir+name)
        shutil.move(fileLDir+label, tarLDir+label)
    return


if __name__ == '__main__':
    fileDir = "/Users/wyw/Documents/陈桂鹏师兄项目/cattle_data/train/images/"  # 源图片文件夹路径
    fileLDir = "/Users/wyw/Documents/陈桂鹏师兄项目/cattle_data/train/labels/"  # 源图片文件夹路径
    tarDir = '/Users/wyw/Documents/陈桂鹏师兄项目/cattle_data/valid/images/'  # 移动到新的文件夹路径
    tarLDir = '/Users/wyw/Documents/陈桂鹏师兄项目/cattle_data/valid/labels/'
    moveFile(fileDir)
