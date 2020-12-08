import cv2
import numpy as np
from slope_finder import finalSlope

# We can simply change the grab_screen dimension instead of doing ROI


#################################################################################

# Only highlight path --> Process the image : Edges
def lane_finder(image, PORx, PORy):

    original_image = image #copy of original image

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_purple = (136,167,155)
    upper_purple = (136,167,243)

    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    lane = cv2.bitwise_and(image, image, mask=mask)

    #Canny and Blurring 
    lane = cv2.cvtColor(lane, cv2.COLOR_HSV2RGB)	
    lane = cv2.cvtColor(lane, cv2.COLOR_RGB2GRAY)
    lane = cv2.Canny(lane, threshold1=200, threshold2=300)
    lane = cv2.GaussianBlur(lane, (3,3), 0 )

    
    # Hough Lines
    lines = cv2.HoughLinesP(lane, 1, np.pi/180, 5, 1)
    
    final_slope, newPORx, newPORy = finalSlope(PORx, PORy, lines)
    
    return final_slope, newPORx, newPORy



#################################################################################


























    

############################################################################3
# Image has (0, 510, 170, 640)
    #Determining the ROI - only in front of the car
    #vertices = np.array([[60, 580], [60, 610], [110, 610], [110, 580]], np.int32)
    

    #lane = roi(lane, [vertices])
    
    '''
    # Hough Lines
    line = cv2.HoughLinesP(lane, 1, np.pi / 180, 40, 0.5)
    draw_lines(lane, line)
    '''

#########################################################################3#########
def lane_finder_pic(image):

    image = cv2.imread(image)
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_purple = (136,167,155)
    upper_purple = (136,167,243)

    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    lane = cv2.bitwise_and(image, image, mask=mask)

    #Canny and Blurring 
    lane = cv2.cvtColor(lane, cv2.COLOR_HSV2RGB)	
    lane = cv2.cvtColor(lane, cv2.COLOR_RGB2GRAY)
    lane = cv2.Canny(lane, threshold1=200, threshold2=300)
    lane = cv2.GaussianBlur(lane, (3,3), 0 )
    
    # Hough Lines
    line = cv2.HoughLinesP(lane, 1, np.pi / 180, 40, 0.5)
    draw_lines(lane, line)
    # ADD try&except when there are no lines

    cv2.imwrite('check2.png', lane)
    print (lane.shape)

#lane_finder_pic('lane_example.png')



'''
def contour_lines(image):
    image = cv2.imread(image)
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_purple = (136,167,155)
    upper_purple = (136,167,243)
    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    lane = cv2.bitwise_and(image, image, mask=mask)

    lane = cv2.cvtColor(lane, cv2.COLOR_HSV2RGB)	
    lane = cv2.cvtColor(lane, cv2.COLOR_RGB2GRAY)
    lane = cv2.Canny(lane, threshold1=200, threshold2=300)
    lane = cv2.GaussianBlur(lane, (3,3), 0 )
    
    thresh = cv2.threshold(lane, 120, 255, cv2.THRESH_BINARY_INV)[1]

    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    print (cnts)

    lines = 0
    for c in cnts:
        cv2.drawContours(lane, [c], -1, (36,255,12), 3)
        lines += 1
        print (len(c))

    print(lines)
    cv2.imshow('thresh', thresh)
    #cv2.imshow('image', lane)
    cv2.waitKey()

new_line('lane_example.png')
'''
def roi(image, vertices):
    mask = np.zeros_like(image)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(image, image, mask)
    return masked

#################################################################################

def roi2(image, vertices):
    image = cv2.fillPoly(image, vertices, (0, 0, 0))
    return image

#################################################################################

def roi3(image, vertices):
    
    # vertices - location of the corners of the roi
    (x,y,w,h) = cv2.boundingRect(vertices)

    vertices = vertices - vertices.min(axis=0)
    mask = np.zeros(image.shape, np.uint8)
    cv2.drawContours(image, [vertices], -1, (255, 255, 255), -1, cv2.LINE_AA)
    result = cv2.bitwise_and(image, image, vertices)

    return result

#################################################################################

def roi4(image):
    rectangle = np.array([(60, 580), (110, 580), (60, 620), (110, 620)])
    mask = np.zeros_like(image)
    cv2.fillPoly(image, [rectangle], 255)
    masked_image = cv2.bitwise_and(image, image, mask)
    return masked_image
    
#################################################################################

    
