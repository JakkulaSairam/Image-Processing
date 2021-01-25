import cv2
import numpy as np

def sharpen(image):
    kernel=np.array([[0,-1,],[-1,5,-1],[0,-1,0]])
    new_image=cv2.filter2D(image,-1,kernel)
    cv2.imshow("sharpened image",new_image)
    cv2.waitKey(0)


def blur(image):
    kernels=[3,5,9,13]
    for idx,k in enumerate(kernels):
        image_bl=cv2.blur(image,ksize=(k,k))
        cv2.imshow(str(k),image_bl)
    return
def resize(fname,width,height):
    image=cv2.imread(fname)
    #cv2.imshow('original image',image)
    # original image
    cv2.waitKey(0)
    org_height,org_width=image.shape[0:2]
    print("width: ",org_width)
    print("height: ",org_height)

    if org_width>=org_height:
        new_image=cv2.resize(image,(width,height))
    else:
        new_image=cv2.resize(image,(height,width))
    
    return fname ,new_image 



filename ,new_image=resize('image.png',400,400)
#cv2.imshow("resized Image",new_image)
cv2.waitKey(0)
#blur(new_image)
cv2.waitKey(0)
sharpen(new_image)
