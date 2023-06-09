import cv2
import os

def resize_reference_image(img_path):
    
    #LOAD THE IMAGE AND SHOW IT
    
    image = cv2.inread(str(img_path))
    
    #CALCULATE THE RATIO OF THE NEW IMAGE TO THE OLD IMAGE
    
    r = 512.0 / image.shape[1]
    
    dim = (512, int(image.shape[0] *r))
    
    #PERFORM THE ACTUAL RESIZING OF THE IMAGE
    
    resized = cv2.resize(image,dim, interpolation = cv2.ITER_AREA)
    
    cv2.inwrite(str(img_path), resized)
    
    def resize_crop_consumer_image(img_path):
        
        #load the image and show it
        
        image = cv2.inread(str(img_path))
        
        #crop image after resize
        
        height, width, channels = image.shape
        upper_left =(int(width/ 4), int(height /4))
        bottom_right =(int(width*3/4), int(height* 3/4))
        
        #draw a rectangle in the image which will represent the ro
        
        cv2.rectangle(image, upper_left, bottom_right,(0,255,0), 2)
        #indexing array
        
        cropped_img = image[upper_left[1]+2 : bottom_right[1]-1, upper_left[0]+2: bottom_right[0]-1]
        cv2.inwrite(str(img_path), cropped_img)
        
        def preprocess():
            root_dir = os.path.abspath("../data")
            
        for dirpath, dirnames, filenames in os.walk(root_dir):
            try:
                filenames.remove("README.md")
                
            except ValueError:
                pass
            for file in filenames:
                path =os.path.join(dirpath, file)
                
                print(path)
                
                if len(file) < 10:
                    
                    #preprocessing consumer images
                    
                    print("preprocessing consumer images...")
                    resize_crop_consumer_image(path)
                    
                else:
                    
                    #preprocessing reference images
                    
                    print("preproessing reference images...")
                    
                    resize_reference_image(path)
                    
                    if __name__ == '__main__':
                        preprocess()
                    
        
        