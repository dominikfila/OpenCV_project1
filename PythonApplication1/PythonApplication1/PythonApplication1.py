import cv2

template = cv2.resize(cv2.imread('assets/triangle.png', 0), (0, 0), fx=0.3, fy=0.3)
h, w = template.shape
i=0
loc= (0,0)
methods = [ cv2.TM_CCOEFF_NORMED]


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for method in methods:
               

        result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if method in [ cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc


        bottom_right = (location[0] + w, location[1] + h) 
        cv2.rectangle(frame, location, bottom_right, 255, 5)
       
        
        cv2.putText(frame,str(method), bottom_right, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, 2) #text
               
 
        cv2.imshow('frame', frame)
        #cv2.waitKey(0)

    if cv2.waitKey(1) == ord('q'):
        break

