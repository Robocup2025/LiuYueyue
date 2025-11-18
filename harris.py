import cv2
import numpy as np

def manual_harris(img_path,k=0.04,thresh=1e-5):
    img=cv2.imread(img_path)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray=np.float32(gray)
    
    Ix=cv2.Sobel(gray,cv2.CV_64F,1,0)
    Iy=cv2.Sobel(gray,cv2.CV_64F,0,1)
    
    Ixx=Ix*Iy
    Iyy=Iy*Iy
    Ixy=Ix*Iy
    
    detM=Ixx*Iyy-Ixy**2
    traceM=Ixx+Iyy
    R=detM-k*(traceM**2)
    
    img_copy=img.copy()
    img_copy[R>thresh*R.max()]=[0,0,255]
    cv2.imwrite('harris_result.png',img_copy)
    return img_copy
    
if __name__=="__main__":
    manual_harris("photo.png")
