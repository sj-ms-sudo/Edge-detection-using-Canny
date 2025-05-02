import cv2 as cv
capture = cv.VideoCapture(1)  #Loading Camera "0 for default webcam"
while True: #looping through each frames
    isTrue, frame = capture.read()  #loading each frames to a variable
    cv.imshow("Live feed",frame) #Displaying live feed onto a window
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY) #converting frames to grayscale for easier processing
    canny = cv.Canny(gray,125,175) #Using canny for edge detection 
    cv.imshow("Edges",canny)   #Displaying Edges 
    if cv.waitKey(1) and 0xFF==27: #exit on pressing esc
        break
capture.release()
cv.destroyAllWindows()