import cv2
import numpy as np
import matplotlib.pyplot as plt


cornell = cv2.imread("cornell.png")
cornell = cv2.resize(cornell,(700,700))
toronto = cv2.imread("toronto.jpg")
toronto = cv2.resize(toronto,(700,700))

combo_image = cv2.addWeighted(toronto,0.6,cornell,1,3)
cv2.imshow('results',combo_image)
cv2.waitKey(0)