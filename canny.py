import cv2
import numpy as np

def gaussian_blur(img,k=5,sigma=1):
    return cv2.GaussianBlur(img,(k,k),sigma)
    
def gradient(img):
    Ix=cv2.Sobel(img,cv2.CV_64F,1,0)
    Iy=cv2.Sobel(img,cv2.CV_64F,0,1)
    mag=cv2.magnitude(Ix,Iy)
    ang=cv2.phase(Ix,Iy,angleInDegrees=True)
    return mag,ang
    
def nms(mag,ang):
    H,W=mag.shape
    Z=np.zeros((H,W))
    ang=ang%180
    for i in range(1,H-1):
        for j in range(1,W-1):
            q=255
            r=255
            angle=ang[i,j]
            if(0<=angle<22.5)or(157.5<=angle<=180):
                q=mag[i,j+1]
                r=mag[i,j-1]
            elif 22.5<=angle<67.5:
                q=mag[i+1,j-1]
                r=mag[i-1,j+1]
            elif 67.5<=angle<112.5:
                q=mag[i+1,j]
                r=mag[i-1,j]
            elif 112.5<=angle<157.5:
                q=mag[i-1,j-1]
                r=mag[i+1,j+1]
            if mag[i,j]>=q and mag[i,j]>=r:
                Z[i,j]=mag[i,j]
    return Z
    
def double_threshold(img,low,high):
    res=np.zeros(img.shape)
    strong=255
    weak=50
    strong_i,strong_j=np.where(img>=high)
    weak_i,weak_j=np.where((img<=high)&(img>=low))
    res[strong_i,strong_j]=strong
    res[weak_i,weak_j]=weak
    return res,weak,strong
    
def hysteresis(img,weak,strong=255):
    H,W=img.shape
    for i in range(1,H-1):
        for j in range(1,W-1):
            if img[i,j]==weak:
                if ((img[i+1,j-1]==strong) or (img[i+1,j]==strong) or (img[i+1,j+1]==strong) or (img[i,j-1]==strong) or (img[i,j+1]==strong) or (img[i-1,j-1]==strong) or (img[i-1,j+1]==strong)):
                    img[i,j]=strong
                else:
                    img[i,j]=0
    return img
    
def manual_canny(img_path):
    img=cv2.imread(img_path,0)
    blur=gaussian_blur(img)
    mag,ang=gradient(blur)
    nms_img=nms(mag,ang)
    dt,weak,strong=double_threshold(nms_img,50,120)
    final=hysteresis(dt,weak,strong)
    final_8u=np.uint8(final)
    cv2.imwrite('canny_result.png',final_8u)
    return final_8u
    
if __name__=='__main__':
    manual_canny("photo.png")
