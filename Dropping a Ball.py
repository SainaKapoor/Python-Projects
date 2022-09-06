# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 16:54:08 2022

@author: Saina Kapoor
"""

#PART A
import matplotlib.pyplot as plt
import numpy as np


def getInput():
    initial_height = float(input("Initial height of the ball: "))
    while initial_height<0:
        print("The height has to be a positive number")
        initial_height = float(input("Initial height of the ball: "))
        
    
     
    
    u = float(input("Initial speed of the ball: "))
    while u<0:
        print("The initial velocity has to be a positive number")
        u = float(input("Initial speed of the ball: "))
       
    
   
    return initial_height,u
        
        
        
def motionSimulator():
    
    
    initial_height,u=getInput()
    #initial_height, u = 20, 0
    ball_falling = True           #setting the condition of 'fall' to true
    g1 = 10 #for falling ball
    g2 = -10 #for rising ball
    t=0   #running time
    height = []
    time = []
    
    time_interval1 = 0   #extremum time for falling
    time_interval2 = 0   #extremum time for rising
    
    for step_time in np.arange(0, 401, 1):
        
        
        if ball_falling == True:    #Scenario for falling ball
            d = u*time_interval1 + 0.5*g1*time_interval1**2      #total distance travelled
            present_height=initial_height-d   #h2= height at the particular position
            t = t + 0.04
            if present_height<=0:
                
                present_height = 0
                ball_falling = False    #to set it for rise of the ball
                
                
                v1= u+g1*time_interval1
             
                
                print("B:")
                print(" The speed is: ", v1)
                print("The total number of timesteps taken are: ", step_time)
                print("The time interval from previous extremum needed to make that motion is: ", time_interval1)
                print("total time passed so far: ", t)
                time_interval1 = 0   #to set it for the next extremum
            time_interval1 = time_interval1 + 0.04
            height.append(present_height)
            time.append(t)
        
        else:
            
            d = v1*time_interval2 + 0.5*g2*time_interval2**2
            
            present_height = d
            present_speed = v1 + g2*time_interval2
            t = t + 0.04
            if present_speed <=0:  #thte ball has reached or approaching the top
                present_speed = 0
                
                ball_falling = True
                
                initial_height = present_height
                u = 0
                print("T:")
                print("The speed is: ", present_speed)
                print("The total number of timesteps taken are: ", step_time)
                print("The time interval needed to make that motion from prev extremum is: ", time_interval2)
                print("total time passed so far: ", t)
                time_interval2=0
            time_interval2 = time_interval2 + 0.04
            height.append(present_height)
            time.append(t)
             
    return time,height
     
    
    

def main():
    
    time, height = motionSimulator()
    plt.plot(time, height, 'bo')
    plt.xlabel('Time[s]')
    plt.ylabel('Height[m]')
    plt.show()

main()