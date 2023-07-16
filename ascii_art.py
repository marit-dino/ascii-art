import cv2
import numpy as np
import math


nums = 64 #128 64
pxs = 16 #8 16
fsize = 0.5 #0.25 0.5

cap = cv2.VideoCapture(0)

if(cap.isOpened() == False):
    print("could not open video capture")


while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        height, width = frame.shape[:2]

        alpha = math.floor(frame.shape[0]/nums)
        
	#to black and white
        img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        img = cv2.GaussianBlur(img, (7, 7), 0)

        # width and height
        w, h = (nums, nums)

        temp = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)

	# initialize image
        img  = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

       
        
        blank =  np.zeros([nums * pxs, nums * pxs,3],dtype=np.uint8)
        blank.fill(255)
        chars = ['@', '#', '+', ':', ',', '.', ' ']


	# choose character depending on brightness of pixel 
        for x in range (0, nums):
            for y in range (0, nums):

                c = chars[6] 

                if(img[x*alpha][y*alpha] < 210):
                    c = chars[5] 

                if(img[x*alpha][y*alpha] < 170):
                    c = chars[4]

                if(img[x*alpha][y*alpha]  < 140):
                    c = chars[3]

                if(img[x*alpha][y*alpha]  < 100):
                    c = chars[2]

                if(img[x*alpha][y*alpha]  < 60):
                    c = chars[1]
                
                if(img[x*alpha][y*alpha]  < 20):
                    c = chars[0]

		# write character at corresponding position
                cv2.putText(
                    blank, 
                    c,
                    (y * pxs + pxs, x * pxs + pxs), 
                    cv2.FONT_HERSHEY_SIMPLEX,
                    fsize, 
                    (0, 0, 0, 255),
                    1) 

        cv2.imshow('Frame', blank)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break;

    else: 
        break


cap.release()
cv2.destroyAllWindows()
