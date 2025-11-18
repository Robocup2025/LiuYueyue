import cv2
import numpy as np

def sobel_filter(img_path):
    img=cv2.imread(img_path,0)
    sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0)
    sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1)
    mag=cv2.magnitude(sobel_x,sobel_y)
    cv2.imwrite('sobel_result.png',mag)
    return mag
    
if __name__=='__main__':
    sobel_filter("photo.png")
