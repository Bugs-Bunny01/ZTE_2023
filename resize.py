import os
import cv2
import numpy as np
# 设置输入文件夹路径，为files.py创建的文件
input_folder = 'D:\desk\data64'

for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.png'):
            # 打开图像并获取其大小
            img_path = os.path.join(root, file)
            img = cv2.imread(img_path)

            height, width, channels = img.shape
            # 根据长边和短边比例计算放大后的尺寸
            if width > height:
                new_width = 1280
                new_height = 720
            else:
                new_height = 1280
                new_width = 720

            # 统一放大为720P图像，并保存处理后的图像
            resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(img_path, resized_img)