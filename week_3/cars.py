#this is a class that describes cars


class car:
    def __init__(self,model,make,year_of_production,fuel_capacity,colour,horse_power):
       self.model = model
       self.make = make
       self.year_of_production =year_of_production
       self.fuel_capacity = fuel_capacity
       self.colour = colour
       self.horse_power = horse_power
    
def print_make(self,make):
    print(" the car is of {0} make" .format(self.make))

def set_make(self,make):
    self.make = make 

def get_make(self):
    return self.make 


def set_colour(self,colour):
    self.make = make 

def get_make(self):
    return self.make





my_car = car("impalla","chevrolet","1969","2500 cc","lilac","390 HP")

friends_car = car("nissan","chevrolet","1970","500 cc","black","465 HP")

my_car.print_make("Nissan")

my_car.set_make("ford")
friends_car.set_make("toyota")

print(my_car.get_make())
print(friends_car.get_make())

my_car.set_colour("blue")
friends_car.set_colour("Pink")

print()

#set the colour and ge colour
#tkinter.....form for registration of students
#displayss