# 在windows测试通过
import os
# 列出指定目录下的所有文件名，确定类别名称
classes = os.listdir('./my_dataset/training_set')
# 打开指定文件，并写入类别名称
with open('./my_dataset/classes.txt','w') as f:
    for line in classes:
        str_line = line +'\n'
        f.write(str_line) # 文件写入str_line，即类别名称

test_dir = './my_dataset/test_set/' # 指定测试集文件路径
# 打开指定文件，写入标签信息
with open('./my_dataset/test.txt','w') as f:
    for cnt in range(len(classes)):
        t_dir = test_dir + classes[cnt]  # 指定测试集某个分类的文件目录
        files = os.listdir(t_dir) # 列出当前类别的文件目录下的所有文件名
        # print(files)
        for line in files:
            str_line = classes[cnt] + '/' + line + ' '+str(cnt) +'\n' 
            f.write(str_line) 

val_dir = './my_dataset/val_set/'  # 指定文件路径
# 打开指定文件，写入标签信息
with open('./my_dataset/val.txt', 'w') as f:
    for cnt in range(len(classes)):
        t_dir = val_dir + classes[cnt]  # 指定验证集某个分类的文件目录
        files = os.listdir(t_dir)  # 列出当前类别的文件目录下的所有文件名
        # print(files)
        for line in files:
            str_line = classes[cnt] + '/' + line + ' ' + str(cnt) + '\n'
            f.write(str_line)  # 文件写入str_line，即标注信息