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
    ReleaseKey(W)

def right(t):
    PressKey(W) #always moving
    PressKey(D)
    #ReleaseKey(A)
    time.sleep(t)
    ReleaseKey(D)
    ReleaseKey(W)

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
        t = 0.15
    else:   
        t = 1 - abs(angle)/90
        t = t*0.2
        t = float("{:.2f}".format(t)) #need only 2 decimal
        print ('time taken :', t)
        
    return t

   
def move(m1, m2):
    # Our initial slope can be assumed infinite (go straight) 
    #m2 - pass the screen/image in main.py

    print ("m1 is {}, m2 is {}".format(m1, m2))

    #angle = math.degrees(math.atan((m1+m2)/(1+(m1*m2))))
    
    print ("angle is :", angle)
    
    
    if m1 == math.inf and m2 == math.inf:
        straight()
        print ('going straight, line62')
        
    elif m1 == math.inf:
        if m2 > 0:
            right(t=0.15)
            print ('turning right, line67')
        elif m2 < 0:
            left(t=0.15)
            print ('turning left, line70')
        else:
            reverse(t=0.2) #constant
            print ('reverseee, line73')

    elif m2 == math.inf:
        if m1 > 0:
            left(t=0.15)
            print ('turning left, line78')
        elif m1 < 0:
            right(t=0.15)
            print ('turning right, line81')
        else:
            reverse(t=0.2) #constant
            print ('reversee, line84')
            
    elif m1 > 0:
        if m2 < 0:
            left(t=timeWRTangle(angle))
            print ('turning left, line89')
        elif m2 > 0:
            if m1>m2:
                right(timeWRTangle(angle))
                print ('turning right, line93')
            elif m1 == m2:
                right(0.15)
                print ('turning right, line96')
            else:
                left(timeWRTangle(angle))
                print ('turning left, line99')
            
        else:
            right(timeWRTangle(angle)) #Right Turn scenario possible
            print ('turning right, line103')

    elif m1 < 0:
        if m2 > 0:
            right(t=timeWRTangle(angle))
            print ('turning right, line108')
        elif m2 < 0:
            if abs(m1)>abs(m2):
                right(timeWRTangle(angle))
                print ('turning right, line112') #wierd
            elif m1 == m2:
                left(0.15)
                print ('turning left, line115')
            else:
                left(timeWRTangle(angle))
                print ('turning left, line118') #wierd
        else:
            left(timeWRTangle(angle)) #Left turn possible
            print ('turning left, line121')

    else:
        reverse(timeWRTangle(angle))
        print (' reverssse, line125')


####################################

    
    
    
            
            

    
