#################### Checker Game ################
def game_Checker(image):
    
    stones_positions = [ [0] * 8 for _ in range(8)]
    temp = image.copy()
    temp = cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)
    h,w = temp.shape
    div = int(w/8)
    
    for i in range(8):
        cv2.circle(temp,(div*(i+1),div*(i+1)),10,(0,0,0))
    display(temp,'Small Circles')
    
    stones = stones_detect(image)
    temp = image.copy()
    for i in range(len(stones)):
        X = stones[i][0]
        Y = stones[i][1]
        S = recognize_stone(image,(X,Y),20)
        
        if S <= 80:
            stones_positions[int(X/74)][int(Y/74)] = 2
            cv2.circle(temp,(stones[i][0],stones[i][1]),10,(0,0,0))
            cv2.line(temp,(X-15,Y-20),(X+15,Y-20),(0,0,0),3)
        else:
            stones_positions[int(X/74)][int(Y/74)] = 1

    stones_positions = np.transpose(stones_positions)
    return stones_positions


######################## GO Game #####################
def game_Go(image):
    stones_positions = [ [0] * 13 for _ in range(13)]
    temp = image.copy()
    temp = cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)
    h,w = temp.shape
    
    div = int(w/14)
    for i in range(14):
        cv2.circle(temp,(div*(i+1),div*(i+1)),10,(0,0,0))
    
    stones = stones_detect(image,1,30,50,20,15,30)
    
    temp = image.copy()
    for i in range(len(stones)):
        X = stones[i][0]
        Y = stones[i][1]
        S = recognize_stone(image,(X,Y),10)
        #cv2.circle(temp,(stones[i][0],stones[i][1]),10,(0,0,0))
        
        if S>150:
            stones_positions[int(X/45)][int(Y/45)] = 1
        #cv2.line(temp,(X-10,Y-15),(X+10,Y-15),(0,0,0),3)
        else:
            stones_positions[int(X/45)][int(Y/45)] = 2

    stones_positions = np.transpose(stones_positions)

    #display(temp)
    return stones_positions

######################## Nine men's Morris Game #############
def game_Morris(image):
    stones_positions = np.zeros(23,dtype = 'int')
    temp = image.copy()
    temp = cv2.cvtColor(temp,cv2.COLOR_BGR2GRAY)
    h,w = temp.shape
    
    center = find_center(temp)
    
    stones = stones_detect(image,1,50,50,22,15,20)
    
    for i in range(len(stones)):
        X = stones[i][0]
        Y = stones[i][1]
        S = recognize_stone(image,(X,Y),10)
        x = 0
        if S > 220:
            x = 1
        else:
            x = 2
        
        if X <= 100:
            if Y > 500:
                stones_positions[0] = x
            elif Y > 260:
                stones_positions[9] = x
            else:
                stones_positions[21] = x
        
        elif X <= 180:
            if Y > 420:
                stones_positions[3] = x
            elif Y > 280:
                stones_positions[10] = x
            else:
                stones_positions[18] = x
        
        elif X <= 280:
            if Y > 330:
                stones_positions[6] = x
            elif Y > 280:
                stones_positions[11] = x
            else:
                stones_positions[15] = x
    
        elif abs(X-300) <= 10:
            if Y > 500:
                stones_positions[1] = x
            elif Y > 420:
                stones_positions[4] = x
            elif Y > 350:
                stones_positions[7] = x
            elif Y < 100:
                stones_positions[22] = x
            elif Y < 170:
                stones_positions[19] = x
            else:
                stones_positions[16] = x

        elif X > 500:
            if Y > 500:
                stones_positions[2] = x
            elif Y > 280:
                stones_positions[14] = x
            else:
                stones_positions[23] = x
                
        elif X > 420:
            if Y > 420:
                stones_positions[5] = x
            elif Y > 280:
                stones_positions[13] = x
            else:
                stones_positions[20] = x

        elif X > 320:
            if Y > 320:
                stones_positions[8] = x
            elif Y > 280:
                stones_positions[12] = x
            else:
                stones_positions[17] = x

    return stones_positions
