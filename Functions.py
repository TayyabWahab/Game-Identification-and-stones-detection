def stones_detect(image,dp=1,dist=50,p1=50,p2=18,minR=20,maxR=40):
    img = image.copy()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img, (3, 3),1)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp, dist, param1 = p1,param2 = p2, minRadius = minR, maxRadius = maxR)
    
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        print(len(circles))
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            cv2.circle(img, (x, y), r, (0, 255, 0), 4)

    #display(img,'Stones Detected')
    return circles

def find_center(image):
    M = cv2.moments(image)
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    
    return((cX,cY))

def recognize_stone(image,center,value):
    X = center[0]
    Y = center[1]
    temp = image.copy()
    temp = cv2.cvtColor(temp,cv2.COLOR_BGR2HSV)
    #avg = int(np.sum(temp[X-15:X+15,Y-20,2])/30)
    avg = temp[X,Y-value,2]
    return avg

def display(image,caption = ''):
    plt.figure(figsize = (10,20))
    plt.title(caption)
    plt.imshow(image)
    plt.show()
