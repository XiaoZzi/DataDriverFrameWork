import os
import shutil


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
    for file_type in get_dir_type(path_org):
        if file_type not in get_dir_type(path_moveto):
            os.makedirs(path_moveto+'\\'+file_type)


def copy_file_and_check(path_org, path_moveto):
    for root, dirt, file in os.walk(path_org):
        for f in file:
            # 得到所有文件的全路径
            f_path = os.path.join(root, f)
            # 得到文件所在的文件夹名称
            file_type = os.path.dirname(f_path).split('\\')[-1]
            shutil.copy2(f_path, path_moveto + '\\' + file_type)

    org_type = set(get_dir_type(path_org))
    moveto_type = set(get_dir_type(path_moveto))

    if not org_type.symmetric_difference(moveto_type):
        print('根据源文件夹结构在%s创建了对应文件夹' % path_moveto)
        if sum([len(x) for _, _, x in os.walk(path_org)]) == sum([len(x) for _, _, x in os.walk(path_moveto)]):
            print('复制后与源文件夹文件总数相同')
        elif sum([len(x) for _, _, x in os.walk(path_org)]) > sum([len(x) for _, _, x in os.walk(path_moveto)]):
            print('复制后文件个数小于源文件夹文件总数，可能源文件夹有重名文件')
        else:
            print('复制后文件个数大于源文件夹文件总数，233333333~')


touch_dir_type(path_org='F:\\testdir', path_moveto='F:\\type')
copy_file_and_check(path_org='F:\\testdir', path_moveto='F:\\type')