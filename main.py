from gaussian import compare_multiple_kernels
from convolution import gaussian_filter_demo
from padding import padding_demo 

if __name__=="__main__":
    print("TASK2:")
    compare_multiple_kernels(sizes=[3,5,7],sigmas=[0.5,1.0,2.0])
    
    print("TASK3:")
    gaussian_filter_demo("photo.png")
    
    print("TASK4:")
    padding_demo("photo.png")
    
