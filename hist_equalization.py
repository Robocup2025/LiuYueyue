import cv2
import numpy as np
import matplotlib.pyplot as plt

def manual_hist_equalization(img):
    if len(img.shape)==3:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        gray=img.copy()
    hist=np.zeros(256)
    h,w=gray.shape
    for i in range(h):
        for j in range(w):
            hist[gray[i,j]]+1
    hist_norm=hist/(h*w)
    cdf=np.cumsum(hist_norm)
    equalized=np.zeros_like(gray)
    for i in range(h):
        for j in range(w):
            equalized[i,j]=np.round(cdf[gray[i,j]]*255)
    return gray,equalized,hist,cdf
    
def visualize_hist_equalization(img_path):
    img=cv2.imread(img_path)
    gray,eq_img,hist,cdf=manual_hist_equalization(img)
    plt.figure()
    
    plt.subplot(2,2,1)
    plt.title("Original Gray Image")
    plt.imshow(gray,cmap='gray')
    plt.axis('off')
    
    plt.subplot(2,2,2)
    plt.title("Equalized Image")
    plt.imshow(eq_img,cmap='gray')
    plt.axis('off')
    
    plt.subplot(2,2,3)
    plt.title("Original Histogram")
    plt.plot(hist)
    
    plt.subplot(2,2,4)
    plt.title("CDF")
    plt.plot(cdf)
    
    plt.tight_layout()
    plt.savefig("hist_equalization_result.png")
    plt.show()
    
    return eq_img
    
if __name__=='__main__':
    visualize_hist_equalization("photo.png")
