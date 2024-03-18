#program to show description of items and value
#name : Susan Maina
#date :28/02/2024

laptop = {"make" :"hp","colour" :"grey", "weight" : "1.2",
             "year" : "2023"}

print(laptop["make"])
print(laptop["colour"])
print(laptop["year"])

#change values in a dictionary

laptop ["colour"] = "red"
laptop["year"] = "2009"
print(laptop)

laptop["size"] = "1200mm x 600mm"
print(laptop)

del laptop ["colour"]

print(laptop)

siz_laptop = laptop.copy
print(siz_laptop)

"""
for key , value in laptop.items() :
    print(key)
    print("\n")
    print(value)
"""

#craete a tuple of your hobbies...then print
#using dictionaries describe your fav car
#print individual values 
#copy the dictionary into another 



