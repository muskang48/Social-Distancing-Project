# -*- coding: utf-8 -*-
"""detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fXRYbcRsnaNJQZbMoXV21x1uZuoSnFRS
"""

# import the necessary packages
#from .social_distancing_config import NMS_THRESH
#from .social_distancing_config import MIN_CONF
import numpy as np
import cv2
# base path to YOLO directory
MODEL_PATH = "yolo-coco" #importing yolo model
# initialize minimum probability to filter weak detections along with
# the threshold when applying non-maxima suppression
allowed_CONF = 0.3 #Min configuration
allowed_NMS_THRESH = 0.3 #min threshold

def detect_people(frame, net, ln, personIdx=0):
	results = []
	(H, W) = frame.shape[:2] #taking part of frame
	getblob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
		swapRB=True, crop=False)
	net.setInput(getblob)
	Outputslayer = net.forward(ln)
	#print(outputslayer
	# detected bounding boxes, centroids, and confidences, respectively initilized
	boxes = []
	confidences = []
	centroids = []
  #layer outputs iterated using for loop
	for output in Outputslayer:
		# detections iterated using for loop
		for getdetection in output:
			#print(output,getdetection)
			#class ID and confidence is extracted  of the current object detection
			getscores = getdetection[5:]
			#print(getscores)
			classID = np.argmax(getscores)
			#print(classID)
			confidence = getscores[classID]
			#  detecting pixel distance is less then min conf
			if classID == personIdx and confidence > allowed_MIN_CONF:
				box = getdetection[0:4] * np.array([W, H, W, H])
				(centerX, centerY, width, height) = box.astype("int")
				#left corner of the bounding box and use the center (x, y)-coordinates to derive the top
				x = int(centerX - (width / 2))
				y = int(centerY - (height / 2))
				#print(x,y)
				#bounding box coordinates,centroids, and confidences is updated
				boxes.append([x, y, int(width), int(height)])
				centroids.append((centerX, centerY))
				confidences.append(float(confidence))
    # apply non-maxima suppression
	cvidxs = cv2.dnn.NMSBoxes(boxes, confidences, allowed_MIN_CONF, allowed_NMS_THRESH)
	# ensure at least one detection exists
	if len(cvidxs) > 0:
		# loop over the indexes we are keeping
		for i in cvidxs.flatten():
			#print(len(cvidxs,i)
			#bounding box coordinates is extracted
			(x, y) = (boxes[i][0], boxes[i][1])
			(w, h) = (boxes[i][2], boxes[i][3])
			#print(X,y,w,h)
			# prediction of centroid probability, bounding box coordinates
			r = (confidences[i], (x, y, x + w, y + h), centroids[i])
			results.append(r)
	#print(results)
	#list of results will be returned
	return results