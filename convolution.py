import numpy as np
import cv2
import matplotlib.pyplot as plt
from gaussian import gaussian_kernel

def convolution(img,kernel):
    H,W=img.shape
    k=kernel.shape[0]//2
    padded=np.pad(img,k,mode='constant')
    out=np.zeros_like(img)
    for i in range(H):
        for j in range(W):
            region=padded[i:i+kernel.shape[0],j:j+kernel.shape[1]]
            out[i,j]=np.sum(region*kernel)
    return out
    
def gaussian_filter_demo(img_path):
    img=cv2.imread(img_path,0)
    sizes=[3,5,7]
    sigmas=[0.5,1.0,2.0]
    
    for size,sigma in zip(sizes,sigmas):
        kernel=gaussian_kernel(size,sigma)
        filtered=convolution(img,kernel)
        
        plt.figure()
        
        plt.subplot(1,2,1)
        plt.imshow(img,cmap='gray')
        plt.title("Original")
        
        plt.subplot(1,2,2)
        plt.imshow(filtered,cmap='gray')
        plt.title(f"Gaussian Blur(size={size},sigma={sigma})")
        plt.show()

if __name__=="__main__":
    gaussian_filter_demo("photo.png")
