#program to show functions
#name : Susan Maina
#date :29/02/2024


#block of code runnning together as a unit

#user defined function and built in function

#defininig the function

def print_name():
    print("my name is Susan Maina")

#calling the function
print_name()


def print_details(name , age, id ,gender):
    print("i am {0} , {1} years old , my id no is {2} and gender is {3}".format(name ,age ,id ,gender))


print_details("Susan Maina" , "18 ","5685577" ,"female")


print_details("Lucy Ngari" , "78 ","5685577" ,"female")

def sum_num(x,y):
    return x + y

z = sum_num(10,20)
print(z)

def prod_num(x,y):
    return x * y
print(prod_num(50,65))

def print_odds(first_num,last_num):
    for i in range(first_num, last_num):
        print(i %2 )

print_odds(0,15)

#print odd numbers
#write a function to print all prime numbers form 1-99
#function to print all squares ,cubes of no btwn 1-10
#function to cvalculate sa of cylinder cone cube sphere...volume of the four
