from datetime import timedelta
from csvreader import *


#  creates a Truck class
class Truck:
    def __init__(self, location, hub_departure, miles, assoc_packages=[]):
        self.location = location
        self.hub_departure = hub_departure
        self.miles = miles
        self.assoc_packages = assoc_packages


#  creates a list of package IDs for each truck
truck_1_packages = ['29', '30', '31', '34', '37', '40', '1', '14', '16', '20', '13', '15', '19', '27', '35', '39']
truck_2_packages = ['3', '18', '36', '38', '6', '25', '32', '28', '4', '12', '17', '24', '26']
truck_3_packages = ['9', '2', '5', '7', '8', '10', '11', '21', '22', '23', '33']

#  creates truck objects for truck1, truck2, and truck3
truck1 = Truck('4001 South 700 East', timedelta(hours=8), 0, truck_1_packages)
truck2 = Truck('4001 South 700 East', timedelta(hours=9, minutes=10), 0, truck_2_packages)
truck3 = Truck('4001 South 700 East', timedelta(hours=10, minutes=30), 0, truck_3_packages)


#  loops through all of the packages, finds the nearest neighbor (address), and delivers their package
def nearest_neighbor(truck):
    i = 0  # initializes i to 0
    current_truck_distance = float(truck.miles)  # initializes current_truck_distance to current miles of truck.
    current_time = truck.hub_departure  # initializes current_time to the trucks hub departure time.
    current_distance = float(100)  # initializes current_distance to 100
    while len(truck.assoc_packages) != 0:
        while i < len(truck.assoc_packages):
            current_address = truck.location  # sets the current address as the trucks location

            current_package = h.lookup(truck.assoc_packages[i])  # selected package
            package_address = current_package.package_address  # address of selected package

            new_distance = get_distance(current_address, package_address)  # calls get_delivery function

            # checks if the current distance is larger than the new distance.
            # if so, sets variables to new values.
            if float(current_distance) > float(new_distance):
                current_distance = float(new_distance)
                location = package_address
                package = current_package
                value = truck.assoc_packages[i]
            i = i + 1
        i = 0  # sets i back to the initial value of 0

        truck.location = location  # sets trucks location to the last package delivered
        truck.assoc_packages.remove(value)  # removes delivered package from truck
        current_truck_distance = current_truck_distance + float(
            current_distance)  # adds the distance to the mileage count
        current_time = package.delivery_time = current_time + time_calculator(
            current_distance)  # records time of delivery

        current_distance = float(100)  # sets distance back to the initial value of 100

    # checks if truck is empty. If so, returns truck to hub and mileage to the truck.
    if len(truck.assoc_packages) == 0:
        return_to_hub = get_distance(current_address, '4001 South 700 East')  # gets the distance back to the hub
        current_truck_distance = current_truck_distance + float(return_to_hub)  # adds the distance to the mileage count
        truck.miles = current_truck_distance  # sets the trucks miles equal to the overall miles travelled


# gets and returns the distance between two addresses
def get_distance(current_address, package_address):
    if address_lookup(package_address) > address_lookup(current_address):
        current_distance = distance_data[address_lookup(package_address)][
            address_lookup(current_address)]
    else:
        current_distance = distance_data[address_lookup(current_address)][
            address_lookup(package_address)]
    return current_distance


#  calculates the time it takes to reach an address by the miles travelled
def time_calculator(miles):
    time = miles / 18
    return timedelta(hours=time)
