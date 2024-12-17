import os
import shutil
# 列出指定目录下的所有文件名，确定分类信息
classes = os.listdir('./my_newphoto')

# 定义创建目录的方法
def makeDir(folder_path):
    if not os.path.exists(folder_path):  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(folder_path)

# 指定文件目录
read_dir = './my_newphoto/' # 指定原始图片路径
train_dir = './my_dataset/training_set/' # 指定训练集路径
test_dir = './my_dataset/test_set/'# 指定测试集路径
val_dir = './my_dataset/val_set/'# 指定验证集路径

for cnt in range(len(classes)):
    r_dir = read_dir + classes[cnt] + '/'  # 指定原始数据某个分类的文件目录
    files = os.listdir(r_dir)  # 列出某个分类的文件目录下的所有文件名
    # files = files[:4000]
    # 按照6:2:2拆分文件名,可更换比例
    offset1 = int(len(files) * 0.6)
    offset2 = int(len(files) * 0.8)
    training_data = files[:offset1]
    val_data = files[offset1:offset2]
    test_data = files[offset2:]

    # 根据拆分好的文件名新建文件目录放入图片
    for index,fileName in enumerate(training_data):
        w_dir = train_dir + classes[cnt] + '/'  # 指定训练集某个分类的文件目录
        makeDir(w_dir)
        # shutil.copy(r_dir + fileName,w_dir + classes[cnt] + str(index)+'.jpg')
        shutil.copy(r_dir + fileName, w_dir + str(index) + '.jpg')
    for index,fileName in enumerate(val_data):
        w_dir = val_dir + classes[cnt] + '/'  # 指定测试集某个分类的文件目录
        makeDir(w_dir)
        # shutil.copy(r_dir + fileName, w_dir + classes[cnt] + str(index) + '.jpg')
        shutil.copy(r_dir + fileName, w_dir + str(index) + '.jpg')
    for index,fileName in enumerate(test_data):
        w_dir = test_dir + classes[cnt] + '/'  # 指定验证集某个分类的文件目录
        makeDir(w_dir)
        # shutil.copy(r_dir + fileName, w_dir + classes[cnt] + str(index) + '.jpg')
        shutil.copy(r_dir + fileName, w_dir + str(index) + '.jpg')