# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:00:21 2022

@author: Saina Kapoor
"""

#Question
"""
Suppose object A is traveling towards object B with a speed v. A and B are separated by a distance d. If A
is decelerating by a value of a , we want to determine if it will hit the object B. The user must provide the
following values d, v and a. d is in the range [5,10],
a is in the range [-100,0] and v is in the range
[1,10]. The distance travelled by the object A in
time t (a positive number less than 10 that is also
to be received from the user) can be calculated as
𝑠 = max(0, 𝑣𝑡 + 0.5𝑎𝑡!)

If s is greater than or equal to d then the object
will collide. Write a python program that does
the following: (i) determines if the objects collide
for a given set of d, v, a and t. (ii) for a given value
of d and v, and starting with a = -50, determines
the critical value of a at which A will just touch B.
Hint: To find the critical value of a, keep increasing a by a small amount (example, 0.2 ), and for each
value of a scan through a long range of t to conclusively establish if the object A hits B or not. Note: All
values are floating point data.

"""


import numpy as np

#Defining function with d,a,v,t parameters
def part_one(d,a,v,t):
    s=max(0, v*t + 0.5*a*t*t)

    #Applying condtion to check for the collision
    if s>d or s==d:
        print("\n i. The object collided!!! \n" )
    else:
        print(" i. The object got missed!!! \n")
  
#Defining function with only d and v as a parameter
def part_two(d,v):
    
    #Applying nested for loop so that the object remains within time limit and check for the critical value
    
    for a in np.arange(-50.0, 0.0, 0.2):
        for t in range(1,11):
        
            s=max(0, v*t + 0.5*a*t*t)
           
            if s>d or s==d:
                print(" ii. The object collided!!! and the distance travelled is : " '%.2f' %s + " where critical point of acceleration is:" '%.2f' %a + " and time is: " '%.2f' %t )
                break
            
       
        
        
def main():
    
    #asking for user's input with input validation
    distance= float(input("Type the distance between the object A and B in the range of 5 to 10: "))
    while distance <5 or distance > 10:
        print("Invalid value, Please try again")
        distance= float(input("Type the distance between the object A and B in the range of 5 to 10: "))

    acceleration= float(input("Type the acceleration of the object A in the range of -100 to 0: "))
    while acceleration <-100 or acceleration > 0:
        print("Invalid value, Please try again")
        acceleration= float(input("Type the acceleration of the object A in the range of -100 to 0: "))
  
    velocity= float(input("Type the velocity the object A in the range of 1 to 10: "))
    while velocity <1 or velocity > 10:
       print("Invalid value, Please try again")
       velocity= float(input("Type the velocity the object A in the range of 1 to 10: "))

    time= float(input("Type the time travelled by the object A in the range of 1 to 10: "))
    while time <1 or time > 10:
        print("Invalid value, Please try again")
        time= float(input("Type the time the object A in the range of 1 to 10: \n")) 
    
    #calling functions
    part_one(distance, acceleration, velocity, time)
    part_two(distance, velocity)
   
    
main()
    



