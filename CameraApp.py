#!/usr/bin/env python
# coding: utf-8

# In[7]:


import cv2

# Start capturing webcam
cap = cv2.VideoCapture(0)

''' We can set the width and height as well
 For width, id is 3 and for height, id is 4 '''
# Setting width
cap.set(3, 1024)
cap.set(4, 720)
# We can set the brightness, id for that is 10
cap.set(10, 200)

# Capturing photo for each milisecond and runing for each mili second to for a stream video
while True:
    # Capturing photo
    status, photo = cap.read()
    # Showing photo
    cv2.imshow('ankush.jpg', photo)
    # Capturing photo for each milisecond
    cv2.waitKey(1)
    # Esc key has ascii value 27 hence to close the app window we need to press esc key
    if cv2.waitKey(1) == 27:
        break

# Destroying the output window
cv2.destroyAllWindows()
# Closing the webcam
cap.release()


# In[ ]:


# Installing opencv in current environment
# !pip install opencv-python

