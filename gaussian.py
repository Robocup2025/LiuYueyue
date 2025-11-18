import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_kernel(size,sigma):
    k=size//2
    x,y=np.mgrid[-k:k+1,-k:k+1]
    g=np.exp(-(x**2+y**2)/(2*sigma**2))
    g=g/g.sum()
    return g
    
sizes=[3,5,7]
sigmas=[0.5,1.0,2.0]
    
def compare_manual_opencv(size,sigma):
    opencv_kernel_1=cv2.getGaussianKernel(size,sigma)
    opencv_kernel=opencv_kernel_1 @ opencv_kernel_1.T
    manual_kernel=gaussian_kernel(size,sigma)
    plt.figure()
    
    plt.subplot(1,2,1)
    plt.imshow(manual_kernel,cmap='viridis')
    plt.title(f"Manual(size={size},sigma={sigma})")
    plt.colorbar()
    
    plt.subplot(1,2,2)
    plt.imshow(opencv_kernel,cmap='viridis')
    plt.title(f"OpenCV(size={size},sigma={sigma})")
    plt.colorbar
    
    plt.tight_layout()
    plt.show()
    
    diff=np.sum(np.abs(manual_kernel-opencv_kernel))
    print(f"difference of size={size} and sigma={sigma}:{diff:.6f}")
    
def compare_multiple_kernels(sizes, sigmas):
    for size in sizes:
        for sigma in sigmas:
            compare_manual_opencv(size, sigma)
    
if __name__=="__main__":
    compare_manual_opencv(5,1.0)
