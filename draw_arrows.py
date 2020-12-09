import numpy as np
import cv2
from draw_lanes import draw_lanes

def lane_to_line(image):

    #                                   start     end     color(BGR)  thickness
    our_arrow = cv2.arrowedLine(image, (x1, y1), (x2, y2), (255, 0, 0), 3)

    # Get (x1,y1), (x2, y2) of Left and Right lanes
    # New x1 = (x1_left + x1_right)/2 and so on .....
    
    new_arrow = cv2.arrowedLine(image, (X1, Y1), (X2, Y2), (0, 0, 255), 3)

    
