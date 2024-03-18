#program to run lists 
#name : Susan Maina
#date :28/02/2024

friends = ["jane","susan", "joy", "julie","judith" ]

for friend in friends :
    print(friend)

enemies = friends [:] #to copy one list into another
print(enemies)

fruits = ["guava", "mango" ,"lime","strawberry" ,"pineapple"]

#slice part of the list

print(fruits[0:3])

del fruits[0]

print(fruits)

squares = [] # initializes an empty list

for x in range (0,11) :
    squares.append(x **2)

print (squares)

