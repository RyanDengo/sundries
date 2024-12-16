from PIL import Image
from torchvision import transforms
import os

def makeDir(folder_path):
    if not os.path.exists(folder_path):  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(folder_path)

classes = os.listdir('D:\\tools\\myfiles\\') # 指定原始图片路径  
read_dir = 'D:\\tools\\myfiles\\' # 指定原始图片路径
new_dir = 'D:\\tools\\myfiles\\new_' # 指定新图片路径
for cnt in range(len(classes)):
    r_dir = read_dir + classes[cnt] + '\\'
    print(cnt)
    print(classes[cnt])
    print(r_dir)
    files = os.listdir(r_dir)
    #print(files)
    for index,file in enumerate(files):
        img_path = r_dir + file
        img = Image.open(img_path)   # 读取图片
        resize = transforms.Resize([224, 224])
        IMG = resize(img)
        w_dir = new_dir + classes[cnt] + '\\'       
        makeDir(w_dir)
        save_path = w_dir + str(index)+'.jpg'
        IMG = IMG.convert('RGB')
        IMG.save(save_path)