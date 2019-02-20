import os, shutil, time


def file_classfies(target_path):
    global count
    file_list = os.listdir(target_path)
    for file in file_list:
        os.chdir(target_path)
        if file.find('.') == -1:
            continue
        filetype = file.split('.')[-1]
        if not os.path.exists(filetype):
            os.mkdir(filetype)
        new_path = os.path.join(target_path, '%s' % filetype)
        os.chdir(new_path)
        if os.path.exists(file):
            continue
        else:
            os.chdir(target_path)
            shutil.move(file, filetype)
            count += 1


start = time.time()
count = 0
path = 'G:\picture\mi5splus'
file_classfies(path)
total_time = time.time() - start
print("程序运行时间：%0.2f" % total_time)
print("共处理图片：%d" % count)
