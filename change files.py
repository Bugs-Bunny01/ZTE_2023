import os
import shutil

def move_png_to_subfolder(folder_path):
    subfolder = os.path.join(folder_path, 'png_files')
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.png'):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(subfolder, file)
                shutil.move(src_file, dst_file)

if __name__ == '__main__':
    folder_path = 'C:/Users/17664/Desktop/data'
    move_png_to_subfolder(folder_path)