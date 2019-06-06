import os
import shutil
path = "C:/Users/gao/Desktop/To_Bober"
path_img = path+"/train/"
path_label1 = path+"/label2_3/"
path_label2 = path+"/label5_20/"
path1 = path + "/path1/"
path2 = path + "/path2/"
path3 = path + "/path3/"
shutil.copytree(path_img, path1)
shutil.copytree(path_label1, path2)
shutil.copytree(path_label2, path3)

for file,i in zip(os.listdir(path1),range(0,400,3)):
    os.rename(os.path.join(path1, file), os.path.join(path1, '%d' % int(i) + ".png"))
for file,i in zip(os.listdir(path2),range(1,400,3)):
    os.rename(os.path.join(path2, file), os.path.join(path2, '%d' % int(i) + ".png"))
for file,i in zip(os.listdir(path3),range(2,400,3)):
    os.rename(os.path.join(path3, file), os.path.join(path3, '%d' % int(i) + ".png"))
