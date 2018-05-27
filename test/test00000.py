import os

d_path = 'F:\\type\\black'
dir_type = []

if os.listdir(d_path):
    print('kong')
    print(len(os.listdir(d_path)))
# 如果为空，直接添加最后一个文件夹名称
else:
    d_type = d_path.split('\\')[-1]

    dir_type.append(d_type)
print(dir_type)
print(os.listdir(d_path))