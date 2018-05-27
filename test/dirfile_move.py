import os


def get_dir_type(path):
    dir_type = []
    for root, dirt, file in os.walk(path):
        for f in file:
            # 得到所有文件的全路径
            f_path = os.path.join(root, f)
            # 得到文件所在的文件夹名称
            file_type = os.path.dirname(f_path).split('\\')[-1]
            if file_type not in dir_type:
                dir_type.append(file_type)

    # 如果文件夹为空
        for d in dirt:
            d_path = os.path.join(root, d)
            if os.listdir(d_path):
                pass
                # 如果为空，直接添加最后一个文件夹名称
            else:
                d_type = d_path.split('\\')[-1]
                if type not in dir_type:
                    dir_type.append(d_type)
    return dir_type


def touch_dir_type(path_org, path_moveto):
    # 判断转移的文件夹是否已经创建，如果没有创建则创建
    if not os.path.exists(path_moveto):
        os.makedirs(path_moveto)
    print(get_dir_type(path_org), get_dir_type(path_moveto))
    for file_type in get_dir_type(path_org):
        if file_type not in get_dir_type(path_moveto):
            os.makedirs(path_moveto+'\\'+file_type)


touch_dir_type('F:\\testdir', 'F:\\type')
