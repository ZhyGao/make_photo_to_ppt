import matplotlib.pyplot as plt
from PIL import Image
import os
path = "C:/Users/gao/Desktop/To_Bober/sum/"
namepath = "C:/Users/gao/Desktop/To_Bober/train/"
names=[]
for file,i in zip(os.listdir(namepath),range(1,126)):
    name = file.split('.')[0]
    names.append(name)
for i in range(0,400,3):
    path1=path+"{}.png".format(i)
    path2=path+"{}.png".format(i+1)
    path3=path+"{}.png".format(i+2)
    fig = plt.figure(figsize=(10, 5))
    fig.suptitle("{}".format(names[int(i/3)]),fontsize=20,y=0.9)
    plt.subplot(131)
    plt.title("Angiogram")
    plt.imshow(Image.open(path1))
    plt.axis('off')
    plt.subplot(132)
    plt.title("Pred")
    plt.axis('off')
    plt.imshow(Image.open(path2))
    plt.subplot(133)
    plt.title("New_label")
    plt.axis('off')
    plt.imshow(Image.open(path3))
    plt.savefig('C:/Users/gao/Desktop/To_Bober/ppt/{}.png'.format(names[int(i/3)]),bbox_inches='tight',dpi=1024,pad_inches=0.1)



