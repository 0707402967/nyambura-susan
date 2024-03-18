# a programme to solve volume of a cylinder
#name: Susan Maina
#date :20/02/2024

import math 

#cylinder

pi = 3.14
r= float(input("enter the value of the radius"))
h=float(input(" enter the vallue of the height"))
r_sq =(r ** 2)

v=(pi * r_sq *h)
sa= ((2*pi*r*h) + (2*pi * r_sq))
print("the volume of the cylinderis :", v)
print("the surface areaof the cylinder:", sa)


