import numpy as np
import math
from math import sqrt

def slope(x1, y1, x2, y2):
    if x1 == x2:
        m = math.inf
    else:
        m = (y2-y1)/(x2-x1) 

    return m

    
# We will get lines via HoughLinesP
# POR - Point Of Reference
def finalSlope(PORx, PORy, lines):
    total = len(lines)
    print ("Total lines detected :", total)
    sum_dist = 0
    distList = []
    midx_list = []
    midy_list = []
    finalMidX, finalMidY = 0, 0
    #slopes = []

    for line in lines:
        coords = line[0]
        x1, y1, x2, y2 = coords[0], coords[1], coords[2], coords[3]
        #cv2.line(img, (x1, y1), (x2, y2), [255,255,255], 1)
        midx = int((x1+x2)/2)
        midy = int((y1+y2)/2)
        midx_list.append(midx)
        midy_list.append(midy)

        dist = sqrt( (midx - PORx)**2 + (midy - PORy)**2 )
        sum_dist += dist
        distList.append(dist)
    
    for i in range(total):
        finalMidX += ((sum_dist - distList[i])/((total-1)*sum_dist))*midx_list[i]
        finalMidY += ((sum_dist - distList[i])/((total-1)*sum_dist))*midy_list[i]


    final_slope = slope(x1 = PORx, y1 = PORy, x2 = finalMidX, y2 = finalMidY)

##    print ("porx is {}, pory is {}, midx is {} and midy is {}".format(PORx, PORy, finalMidX, finalMidY))
##
##    print ('max X is {} and max Y is {}'.format(max(midx_list), max(midy_list)))
##    print ('min X is {} and min Y is {}'.format(min(midx_list), min(midy_list)))
##    print ('slopes recorded are :', slopes)
    
    return final_slope, min(midx_list), min(midy_list)

    

        
