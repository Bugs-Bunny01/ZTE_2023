import os
import shutil

# 定义源目录和目标目录
source_dir = 'D:\ZTE\zte'  # 超分后的图像都在当前工作目录下

# 遍历源目录中的文件
for filename in os.listdir(source_dir):
    if filename.endswith('.png'):
        # 解析文件名，获取第一个数字
        num = int(filename.split('_')[0])

        # 根据数字选择目标目录，不存在则创建。目的是将超分后的图像恢复成官方data目录结构
        target_dir = 'D:\desk\data64\{:05d}'.format(num)

        # 如果目标目录不存在，则创建它
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # 移动文件到目标目录
        shutil.move(os.path.join(source_dir, filename), os.path.join(target_dir, filename))