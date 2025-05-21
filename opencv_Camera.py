import cv2                    #Fast you need to Import CV2
video_cap=cv2.VideoCapture(0) #Here we declare the Variable
while True:                   # here we use a loop for this function
    ret,video_data=video_cap.read()  # now we put our previous variable store it our new variable .
    cv2.imshow("video_live",video_data)  #compiler show our output and file path name is imshow,here we store video data
    if cv2.waitKey(10)==ord("a"): #we use ord for stop this loop
        break                     # now we break the loop
video_cap.release()               # we declare our funcation