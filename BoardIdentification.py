def detect_game(image,center):
    game = None
    if abs(int(image[center[0]-20,center[1]+20]) - int(image[center[0]+20,center[1]+20])) > 50:
        game = 'Chekers'
    else:
        image = cv2.GaussianBlur(image,(5,5),1)
        try:
            lines = []
            temp = image[center[0]-40:center[0]+40,center[1]-40:center[1]+40]
            temp = cv2.Canny(temp,100,150)
            #display(temp,'Edges')
            lines = cv2.HoughLinesP(image=temp,rho=1,theta=np.pi/180, threshold=10,lines=np.array([]), minLineLength=10,maxLineGap=5)
            if len(lines) > 0:
                game = 'Go'
        except:
            game = 'Morris'
    
    return game

def recognize_stone(image,center,value):
    X = center[0]
    Y = center[1]
    temp = image.copy()
    temp = cv2.cvtColor(temp,cv2.COLOR_BGR2HSV)
    #avg = int(np.sum(temp[X-15:X+15,Y-20,2])/30)
    avg = temp[X,Y-value,2]
    return avg

def extract_board(image):
    blurred = cv2.GaussianBlur(image, (7, 7), 3)
    thresh = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    thresh = cv2.bitwise_not(thresh)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    board = None
    
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            board = approx
            break
    
    return board
