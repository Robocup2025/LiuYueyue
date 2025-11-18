import numpy as np
import cv2
import matplotlib.pyplot as plt

def padding_zero(img,pad):
    return np.pad(img,pad,mode='constant')
    
def padding_reflect(img,pad):
    return np.pad(img,pad,mode='reflect')
    
def padding_demo(img_path):
    img=cv2.imread(img_path,0)
    pad=30
    p1=padding_zero(img,pad)
    p2=padding_reflect(img,pad)
    plt.figure()
    
    plt.subplot(1,3,1)
    plt.imshow(img,cmap='gray')
    plt.title("Original")
    
    plt.subplot(1,3,2)
    plt.imshow(p1,cmap='gray')
    plt.title("Zero Padding")
    
    plt.subplot(1,3,3)
    plt.imshow(p2,cmap='gray')
    plt.title("Reflect Padding")
    
    plt.show()
    
if __name__=="__main__":
    padding_demo("photo.png")
