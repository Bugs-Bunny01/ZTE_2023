import os
import shutil


src_dir = 'D:\desk\data64'                           #源路径，与fusion.py路径设置相同
dst_dir = 'C:/Users/17664/Desktop/data'              #目标文件路径，官方data路径

#将超分后的图像复制到data文件里
for subdir, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith('.png'):
            src_file = os.path.join(subdir, file)
            dst_file = os.path.join(dst_dir, os.path.relpath(subdir, src_dir), file)
            os.makedirs(os.path.dirname(dst_file), exist_ok=True)
            shutil.copy2(src_file, dst_file)

#用‘-merged’这张图片替换同子文件下的其他所有图像
def copy_first_image(directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.png'):
                first_image = os.path.join(subdir, file)
                break
        for file in files:
            if file.endswith('.png'):
                image_path = os.path.join(subdir, file)
                if not os.path.samefile(first_image, image_path):
                    shutil.copy(first_image, image_path)
            # os.remove(first_image)

copy_first_image('C:/Users/17664/Desktop/data')         #与dst_dir路径设置相同


#删除子文件下第一张图片，也就是‘-merged’这张图片
for subdir, dirs, files in os.walk(dst_dir):
    for dir in dirs:
        dir_path = os.path.join(subdir, dir)
        images = [f for f in os.listdir(dir_path) if f.endswith('.png')]
        if len(images) > 0:
            image_path = os.path.join(dir_path, images[0])
            os.remove(image_path)