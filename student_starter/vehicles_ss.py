from abc import ABCMeta
import csv

#<--------------------------------------------------------------->#
#<---------------------- CLASS DEFINITIONS ---------------------->#
#<--------------------------------------------------------------->#

class Vehicle(metaclass=ABCMeta):
    """Base class

    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        ", "_on: The date the vehicle was ", ".
    """
    
    def __init__(self, make, model, year, mileage):
        """Return a new Vehicle object."""
        # TODO
        pass
    
    def print_info(self):
        """Prints out vehicle data"""
        # FINISHED
        width = 20
        print(f"Make: {self.make}".ljust(width, ' ')         +
              f"Model: {self.model}".ljust(width, ' ')       +
              f"Year: {self.year}".ljust(width, ' ')         +
              f"Mileage: {self.mileage}".ljust(width, ' ')   +
              f"Buy-back price: {self.final_sale_price()}")

    # TODO there's something missing right here...
    def vehicle_type():
        """Return the type of vehicle"""
        # FINISHED
        pass


class Car(Vehicle):
    """Inherits from Vehicle"""
    
    base_sale_price = 5000
    rate = 0.5
    
    def vehicle_type(self):
        # FINISHED
        return "Car"

    def final_sale_price(self):
        """returns the final sale price, which subtracts base_sale_price
        from mileage * rate"""
        # TODO
        pass
    
class Truck(Vehicle):
    """Inherits from Vehicle"""
    
    base_sale_price = 10000
    rate = 0.1
    
    def vehicle_type(self):
        # FINISHED
        return "Truck"

    def final_sale_price(self):
        """returns the final sale price, which subtracts base_sale_price
        from mileage * rate"""
        # TODO
        pass


class Motorcycle(Vehicle):
    """Inherits from Vehicle"""
    
    base_sale_price = 2500
    rate = 0.25
    def vehicle_type(self):
        # FINISHED
        return "Motorcycle"

    def final_sale_price(self):
        """returns the final sale price, which subtracts base_sale_price
        from mileage * rate"""
        # TODO
        pass
    
#<--------------------------------------------------------------->#
#<-------------------- NON-CLASS DEFINITIONS -------------------->#
#<--------------------------------------------------------------->#

def print_unique(vehicles, attribute):
    """prints out unique searches that will yield results
       prints out in a sorted form (strings sort by ASCII)"""
    # TODO

    
def print_matching(vehicles, attribute, user_attr):
    """actually prints the vehicles' data that match the user's preference"""
    # TODO

    
def print_menu():
    "prints the available choices"
    # FINISHED
    
    options = ["All", "Make", "Model", "Year", "Cars", "Trucks", "Motorcycles"]
    for i in range(0, len(options)):
        print(f"{i + 1}. {options[i]}")


def print_vehicles(vehicles, choice):
    """handles printing all vehicles that matches user's preference"""
    # TODO
    
    choices = {1 : "All",  2 : "Make",  3 : "Model", 4 : "Year",
               5 : "Car",  6 : "Truck", 7 : "Motorcycle"}

    # print all vehicles
    if (choice == 1):
        pass
    
    # make, model, or year
    elif (choice >= 2 and choice <= 3):
        pass

    # Either all cars, all trucks, or all motorcycles
    else:
        pass


def read(filename):
    """reads in file data from csv file"""
    # TODO
    
    pass


def main():
    # FINISHED
    vehicles = read("vehicles.csv")
    while (True):
        print_menu()
        choice = int(input(">>> Your choice: "))
        print_vehicles(vehicles, choice)
