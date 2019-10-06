from abc import ABCMeta, abstractmethod
import csv

class Vehicle(metaclass=ABCMeta):
    """A vehicle for sale by Jeffco Car Dealership.

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
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def print_info(self):
        width = 20
        print(f"Make: {self.make}".ljust(width, ' ')         +
              f"Model: {self.model}".ljust(width, ' ')       +
              f"Year: {self.year}".ljust(width, ' ')         +
              f"Mileage: {self.mileage}".ljust(width, ' ')  +
              f"Buy-back price: {self.final_sale_price()}")

    @abstractmethod
    def vehicle_type():
        """Return a string of "Car", "Truck", or "Motorcycle" """
        pass


class Car(Vehicle):

    base_sale_price = 5000
    rate = 0.5
    
    def vehicle_type(self):
        return "Car"

    def final_sale_price(self):
        return Car.base_sale_price - (int(self.mileage) * Car.rate)

    
class Truck(Vehicle):

    base_sale_price = 10000
    rate = 0.1
    
    def vehicle_type(self):
        return "Truck"

    def final_sale_price(self):
        return Truck.base_sale_price - (int(self.mileage) * Truck.rate)


class Motorcycle(Vehicle):

    base_sale_price = 2500
    rate = 0.25
    def vehicle_type(self):
        return "Motorcycle"

    def final_sale_price(self):
        return Motorcycle.base_sale_price - (int(self.mileage) * Motorcycle.rate)

    
def print_matching(vehicles, attribute, user_attr):
    """prints the vehicles' data that match the user's preference"""
    for vehicle in vehicles:
        if (attribute == "Make" and vehicle.make == user_attr or
            attribute == "Model" and vehicle.model == user_attr or
            attribute == "Year" and vehicle.year == user_attr):
            vehicle.print_info()


def print_menu():
    "prints the available choices"
    options = ["All", "Make", "Model", "Year", "Cars", "Trucks", "Motorcycles"]
    for i in range(0, len(options)):
        print(f"{i + 1}. {options[i]}")


def print_vehicles(vehicles, choice):
    choices = {1 : "All",  2 : "Make",  3 : "Model", 4 : "Year",
               5 : "Car",  6 : "Truck", 7 : "Motorcycle"}

    # print all vehicles
    if (choice == 1):
        for vehicle in vehicles:
            vehicle.print_info()
        
    # make, model, or year
    elif (choice >= 2 and choice <= 4):
        print_unique(vehicles, choices[choice])
        user_attr = input(f"Enter a {choices[choice]}: ")
        print_matching(vehicles, choices[choice], user_attr)

    # Either all cars, all trucks, or all motorcycles
    else:
        for vehicle in vehicles:
            if (vehicle.vehicle_type() == choices[choice]):
                vehicle.print_info()


def print_unique(vehicles, attribute):
    """prints out unique searches that will yield results"""
    unique_attributes = set()
    for vehicle in vehicles:
        if (attribute == "Make"):
            unique_attributes.add(vehicle.make)
        elif (attribute == "Model"):
            unique_attributes.add(vehicle.model)
        elif (attribute == "Year"):
            unique_attributes.add(vehicle.year)

    # print out attributes sorted
    attr_sorted = sorted(unique_attributes)
    for attr in attr_sorted:
        print(attr)
    print("")
    return unique_attributes


def read(filename):

    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        titles = next(csv_reader)
        vehicles = []
        for row in csv_reader:
            vehicle_type, make, model = tuple(row[:3])
            year, mileage = tuple(row[3:])
            
            if (vehicle_type == "Car"):
                new_vehicle = Car(make, model, year, mileage)
            elif (vehicle_type == "Truck"):
                new_vehicle = Truck(make, model, year, mileage)
            elif (vehicle_type == "Motorcycle"):
                new_vehicle = Motorcycle(make, model, year, mileage)
            vehicles.append(new_vehicle)

    return vehicles


def main():
    vehicles = read("vehicles.csv")
    while (True):
        print_menu()
        choice = int(input(">>> Your choice: "))
        print_vehicles(vehicles, choice)
