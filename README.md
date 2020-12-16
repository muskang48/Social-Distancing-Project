# Social-Distancing-Project
Social Distancing Detector Tool  
## About the Project
In a fight against COVID-19 Social Distancing detector has proven to be a very effective measure.People are asked to maintain a safe distance from each other.   
This tool helps to monitor social distancing in workplaces,market, public places etc. This tool can monitor if the people are keeping the same distance from each other or not  by analyzing the video stream from the camera. 

Following steps were used to build social distance detection tool:

- **Object Detection** - Detection of all the people in the video stream using open source architecture YOLOV3. 
- **Distance Measurment** - Measure the pairwise distance between all the people who are detected. Distance measurment was done using two techniques. Following are the techniques used.
   1. **Pixel Based** - Based on the pixels distance.
   2. **Bird of Eye View** - To further improve the results bird of eye view is used. In that pixel based distance are mapped to physical distances. 
- **Check for Social Distancing** -  Based on the distance check how many people are following social distancing and display the results for number of people violating social distancing. 

## Requirments 
To run the code following are needed:
```
argparse
Python 3.5.2
numpy 1.14.5
Opencv(CV2) 4.2.0

For people detection:
yolov3.weights, yolov3.cfg files (weights file can be downloaded from 
here : https://pjreddie.com/media/files/yolov3.weights) weight file is not present due to size Issue. 
```
## Demo 
![demo2](https://user-images.githubusercontent.com/61666843/102327359-a24f5e00-3fab-11eb-8ec5-e341ce18a324.gif)

