from sobel import sobel_filter
from canny import manual_canny
from harris import manual_harris
from hist_equalization import visualize_hist_equalization

if __name__=='__main__':
   img='photo.png'
   sobel_filter(img)
   manual_canny(img)
   manual_harris(img)
   visualize_hist_equalization(img)
