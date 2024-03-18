#program to solve sa and volume of sphere
#name : Susan Maina
#date :28/02/2024

import math

r = float(input("enter the radius of the sphere :"))

def sa_sphere(sa_sphere):
    sa_sphere = (4 * 3.14 * r**2)
    print("the surface area of the sphere is{0}".format(sa_sphere))

sa_sphere({0})

def vol_sphere(volume):
    volume = ((4/3) * 3.14 * r**3)
    print("the volume of the sphere is{0}".format(vol_sphere))

vol_sphere({0})