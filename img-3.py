import os
import cv2
import shutil

# 输入文件夹路径
input_folder = 'C:/Users/17664/Desktop/data'

for root, dirs, files in os.walk(input_folder):
    max_img_path = ""
    second_max_img_path = ""
    third_max_img_path = ""
    max_height = 0
    max_width = 0
    second_max_height = 0
    second_max_width = 0
    third_max_height = 0
    third_max_width = 0

    for file in files:
        if file.endswith('.png'):
            # 打开图像并获取其大小
            img_path = os.path.join(root, file)
            img = cv2.imread(img_path)

            height, width, channels = img.shape

            if height >= max_height and width >= max_width:

                third_max_height = second_max_height
                third_max_width = second_max_width
                third_max_img_path = second_max_img_path

                second_max_height = max_height
                second_max_width = max_width
                second_max_img_path = max_img_path

                max_height = height
                max_width = width
                max_img_path = img_path

            elif height >= second_max_height and width >= second_max_width:

                third_max_height = second_max_height
                third_max_width = second_max_width
                third_max_img_path = second_max_img_path

                second_max_height = height
                second_max_width = width
                second_max_img_path = img_path

            elif height >= third_max_height and width >= third_max_width:

                third_max_height = height
                third_max_width = width
                third_max_img_path = img_path

    for file in files:
        if file.endswith('.png'):
            # 打开图像并获取其大小
            img_path = os.path.join(root, file)
            img = cv2.imread(img_path)

            height, width, channels = img.shape

            if height < third_max_height or width < third_max_width:
                os.remove(img_path)
                print(f"Removed {img_path}")

print("Done!")