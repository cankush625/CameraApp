#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2

# Start capturing webcam
cap = cv2.VideoCapture(0)

# Capturing photo for each milisecond and runing for each mili second to for a stream video
while True:
    # Capturing photo
    status, photo = cap.read()
    # Cropping the livestream
    photo = photo[100:330, 220:430]
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

