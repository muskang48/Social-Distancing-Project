#!/usr/bin/env python



# imports
import cv2
import numpy as np

# Function to calculate bottom center for all bounding boxes and transform prespective for all points.
def get_transformed_points(boxes, transformprespective):
    
    bottom_points = []
    for box in boxes:
        pnts = np.array([[[int(box[0]+(box[2]*0.5)),int(box[1]+box[3])]]] , dtype="float32")
        bd_pnt = cv2.perspectiveTransform(pnts, transformprespective)[0][0]
        pnt = [int(bd_pnt[0]), int(bd_pnt[1])]
        bottom_points.append(pnt)
	#print(bottom_points)
	#print(box)
        
    return bottom_points

def cal_dis(pixel1, pixel2, wdistance, hdistance):
    
    h = abs(pixel2[1]-pixel1[1])
    w = abs(pixel2[0]-pixel1[0])
    #print(h,w)
    
    dis_w = float((w/wdistance)*180)
    dis_h = float((h/hdistance)*180)
    #print(dis_w,dis_h)
    
    return int(np.sqrt(((dis_h)**2) + ((dis_w)**2)))

# Function calculates distance between all pairs and calculates closeness ratio.
def get_distances(boxes1, pointsbottom, wdistance, hdistance):
    
    distance_mat = []
    bxs = []
    
    for i in range(len(pointsbottom)):
        for j in range(len(pointsbottom)):
	     #print(i,j)
            if i != j:
                dist = cal_dis(pointsbottom[i], pointsbottom[j], wdistance, hdistance)
                #dist = int((dis*180)/distance)
                if dist <= 150:
                    closeness = 0
                    distance_mat.append([pointsbottom[i], pointsbottom[j], closeness])
                    bxs.append([boxes1[i], boxes1[j], closeness])
                elif dist > 150 and dist <=180:
                    closeness = 1
                    distance_mat.append([pointsbottom[i], pointsbottom[j], closeness])
                    bxs.append([boxes1[i], boxes1[j], closeness])       
                else:
                    closeness = 2
                    distance_mat.append([pointsbottom[i], pointsbottom[j], closeness])
                    bxs.append([boxes1[i], boxes1[j], closeness])
                
    return distance_mat, bxs
 
# Function gives scale for birds eye view               
def get_scale(W, H):
    
    dis_w = 400
    dis_h = 600
    
    return float(dis_w/W),float(dis_h/H)
    
# Function gives count for humans at high risk, low risk and no risk    
def get_count(distances_mat):

    r = []
    g = []
    y = []
    
    for i in range(len(distances_mat)):

        if distances_mat[i][2] == 0:
            if (distances_mat[i][0] not in r) and (distances_mat[i][0] not in g) and (distances_mat[i][0] not in y):
                r.append(distances_mat[i][0])
            if (distances_mat[i][1] not in r) and (distances_mat[i][1] not in g) and (distances_mat[i][1] not in y):
                r.append(distances_mat[i][1])
                
    for i in range(len(distances_mat)):

        if distances_mat[i][2] == 1:
            if (distances_mat[i][0] not in r) and (distances_mat[i][0] not in g) and (distances_mat[i][0] not in y):
                y.append(distances_mat[i][0])
            if (distances_mat[i][1] not in r) and (distances_mat[i][1] not in g) and (distances_mat[i][1] not in y):
                y.append(distances_mat[i][1])
        
    for i in range(len(distances_mat)):
    
        if distances_mat[i][2] == 2:
            if (distances_mat[i][0] not in r) and (distances_mat[i][0] not in g) and (distances_mat[i][0] not in y):
                g.append(distances_mat[i][0])
            if (distances_mat[i][1] not in r) and (distances_mat[i][1] not in g) and (distances_mat[i][1] not in y):
                g.append(distances_mat[i][1])
   
    return (len(r),len(y),len(g))
