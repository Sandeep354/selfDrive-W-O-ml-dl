import math
#from slope_finder import finalSlope
from path_color_coder import lane_finder
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D

def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    time.sleep(0.25)
    ReleaseKey(W)
    
def left(t):
    PressKey(W) #always moving
    PressKey(A)
    #ReleaseKey(D)
    time.sleep(t)
    ReleaseKey(A)
    PressKey(D)
    ReleaseKey(D)
    #ReleaseKey(W)


def right(t):
    PressKey(W) #always moving
    PressKey(D)
    #ReleaseKey(A)
    time.sleep(t)
    ReleaseKey(D)
    PressKey(A)
    ReleaseKey(A)
    #ReleaseKey(W)

def reverse(t):
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    PressKey(S)
    time.sleep(t)
    ReleaseKey(S)


def timeWRTangle(angle):
    #More angle --> less speed --> less time.sleep
    if angle == 'nan':
        t = 0.05
    else:   
        t = 1 - angle/180
        t = t*0.05
        t = float("{:.4f}".format(t)) #need only 2 decimal
        print ('time taken :', t)
        
    return t

def theta(theta_i):
    if theta_i >= 0:
        theta_i = theta_i
    else:
        theta_i = 180 + theta_i

    return theta_i

        
def move2(m1, m2):
    
    theta1 = theta(math.degrees(math.atan(m1)))
    theta2 = theta(math.degrees(math.atan(m2)))
    angle = theta1-theta2
    abs_angle = abs(angle)

    if angle > 0:
        right(timeWRTangle(abs_angle))
        #straight()
        print ('turn RIGHT by angle :', angle)
    elif angle < 0:
        left(timeWRTangle(abs_angle))
        #straight()
        print ('turn LEFT by angle', angle)
    else:
        straight()
        print ('STRAIGHT')
