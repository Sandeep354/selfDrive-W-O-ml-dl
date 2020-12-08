import numpy as np
import cv2
import time
from draw_lanes import draw_lanes
from grabscreen import grab_screen
import os
from path_color_coder import lane_finder
from slope_finder import finalSlope
from drive2 import move2
#from drive import move
from directkeys import PressKey, ReleaseKey, W, A, S, D
from getkeys import key_check
import math

#region_of_interest = (0,510,170,640) #only the mini-map
roi_lanes = (70, 590, 100, 600) #focus on lanes which we need


def main():

    m1 = math.inf #initial slope
    PORx, PORy = 13, 0 # Initial Point Of Reference
    
    for i in list(range(5))[::-1]:
        print(i+1)
        time.sleep(1)
        
    last_time = time.time()
    paused = False
    
    while True:

        if not paused:
            screen = grab_screen(region=roi_lanes)
            #screen = cv2.resize(screen, (160, 120))
            
            #convert from RGB to BGR since lane finder used BGR to HSV
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

            
            try:
                final_slope, newPORx, newPORy = lane_finder(screen, PORx, PORy)
                move2(m1, final_slope)
                m1 = final_slope
                PORx, PORy = newPORx, newPORy
            except:
                print ('line not found')
                ReleaseKey(W)
                PressKey(S)
                time.sleep(0.25)
                ReleaseKey(S)

            '''
            final_slope = lane_finder(screen)
            move2(m1, final_slope)
            m1 = final_slope
            '''

            print('Frame took {} seconds'.format(time.time()-last_time))
            last_time = time.time()

        keys = key_check()

        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)

            
        #cv2.imshow('window', new_screen)
        #cv2.imshow('window2', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
        
    
##        if cv2.waitKey(25) & 0xFF == ord('q'):
##            cv2.destroyAllWindows()
##            break

main()


