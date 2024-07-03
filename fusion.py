import os
import cv2

# 输入文件夹路径，与resize.py路径设置相同
input_folder = 'D:\desk\data64'

for root, dirs, files in os.walk(input_folder):
    # 统计该子文件夹下的所有图像
    img_paths = []
    for file in files:
        if file.endswith('.png'):
            img_path = os.path.join(root, file)
            img_paths.append(img_path)
    if len(img_paths) >= 3:
        # 读取所有图像并计算权重
        imgs = []
        weights = []
        for img_path in img_paths:
            img = cv2.imread(img_path)
            imgs.append(img)

            # 计算权重，可以根据具体需求进行优化
            weight = 1 / (cv2.Laplacian(img, cv2.CV_64F).var() + 1e-6)
            weights.append(weight)

        # 归一化权重
        total_weight = sum(weights)
        weights = [w / total_weight for w in weights]

        # 使用加权平均融合图像
        merged_img = imgs[0] * weights[0]
        for i in range(1, len(imgs)):
            merged_img += imgs[i] * weights[i]

        # 删除原所有图像
        for img_path in img_paths:
            os.remove(img_path)
            print(f"Removed {img_path}")

        # 保存融合后的图像
        output_name = os.path.basename(root) + '_merged.png'
        output_path = os.path.join(root, output_name)
        cv2.imwrite(output_path, merged_img)
        print(f"Saved {output_path}")
print("Done!")