import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    image = cv2.imread('/Users/eapplestroe/Downloads/shiricz-attachments/9.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    board = extract_board(gray)
    
    if len(board) >= 0:
        cv2.drawContours(image, [board], -1, (0, 255, 0), 5)
    else:
        print('No Board Found')
        exit(0)

    display(image,'Board Detected')
    (x, y, w, h) = cv2.boundingRect(board)
    output = gray[y:y+h,x:x+w]
    output = cv2.resize(output,(600,600))

    center = find_center(output)
    game = detect_game(output,center)
    print('Detected Game = '+game)
    display(output)
    
    output = image[y:y+h,x:x+w]
    output = cv2.resize(output,(600,600))
    
    final_matrix = None
    if game == 'Chekers':
        final_matrix = game_Checker(output)

    elif game == 'Go':
        final_matrix = game_Go(output)
    
    else:
        final_matrix = game_Morris(output)

    print('Final Matrix for the Game '+game+' is:')
    print(final_matrix)
