from datetime import timedelta
from csvreader import *
from utils import time_calculator


#  creates a Truck class
class Truck:
    def __init__(self, location, hub_departure, miles, assoc_packages=[]):
        self.location = location
        self.hub_departure = hub_departure
        self.miles = miles
        self.assoc_packages = assoc_packages


#  creates a list of package IDs for each truck
truck_1_packages = ['29', '30', '31', '34', '37', '40', '1', '14', '16', '20', '13', '15', '19', '7', '21', '39']
truck_2_packages = ['3', '18', '36', '38', '6', '25', '32', '28', '4', '12', '17', '24', '26']
truck_3_packages = ['9', '2', '5', '8', '10', '11', '22', '23', '27', '33', '35']

#  creates truck objects for truck1, truck2, and truck3
truck1 = Truck('4001 South 700 East', timedelta(hours=8), 0, truck_1_packages)
truck2 = Truck('4001 South 700 East', timedelta(hours=9, minutes=10), 0, truck_2_packages)
truck3 = Truck('4001 South 700 East', timedelta(hours=10, minutes=30), 0, truck_3_packages)


#  starts the truck routes
def start_routes(time):
    run_route(truck1, time)
    run_route(truck2, time)
    run_route(truck3, time)


#  Complexity - O(n^2)
#  loops through all of the packages, finds the nearest neighbor (address),
#  delivers their package, then re-loops from the new location. This continues until the truck is empty.
def run_route(truck, time):
    i = 0
    current_truck_miles = 0  # initializes current_truck_miles to current miles of truck.
    current_time = truck.hub_departure  # initializes current_time to the trucks hub departure time.
    current_distance = float(100)  # initialize to 100. Represents the closest deliverable location, in miles.

    #  the outer 'while' loops after the truck moves location. Saving the results of the inner while loop.
    #  The inner 'while' loops after finding the distance between the current location and another - keeping the shortest one.
    while len(truck.assoc_packages) != 0:
        while i < len(truck.assoc_packages):
            current_truck_location = truck.location  # sets the current address as the trucks location
            current_package = h.lookup(truck.assoc_packages[i])  # selected package
            package_address = current_package.package_address  # address of selected package
            new_distance = get_distance(current_truck_location, package_address)  # calls get_delivery function

            # checks if the current distance is larger than the new distance.
            # if so, sets variables to new values.
            if float(current_distance) > float(new_distance):
                current_distance = float(new_distance)
                location = package_address
                package = current_package
                value = truck.assoc_packages[i]
            i = i + 1
        i = 0

        truck.location = location  # sets trucks location to the last package delivered
        truck.assoc_packages.remove(value)  # removes delivered package from truck
        current_truck_miles = current_truck_miles + float(current_distance)  # adds the distance to the mileage count
        current_time = package.delivery_time = current_time + time_calculator(current_distance)  # records delivery time
        current_distance = float(100)  # sets distance back to the initial value of 100

        #  if time is not equal to 0, calls the set_package_statuses function. Else, marks package as delivered.
        if time != timedelta(hours=0):
            set_package_status(package, truck, time)
        else:
            package.package_status = 'delivered'

    # checks if truck is empty. If so, returns truck to hub and mileage to the truck.
    if len(truck.assoc_packages) == 0:
        return_to_hub = get_distance(current_truck_location, '4001 South 700 East')  # gets the distance back to the hub
        current_truck_miles = current_truck_miles + float(return_to_hub)  # adds the distance to the mileage count
        truck.miles = current_truck_miles  # sets the trucks miles equal to the overall miles travelled


#  Complexity - O(n)
# gets and returns the distance between two addresses
def get_distance(current_address, package_address):
    if address_lookup(package_address) > address_lookup(current_address):
        current_distance = distance_data[address_lookup(package_address)][
            address_lookup(current_address)]
    else:
        current_distance = distance_data[address_lookup(current_address)][
            address_lookup(package_address)]
    return current_distance


#  Complexity - O(1)
#  changes package statuses to 'delivered' or 'en route'.  'at the hub' is the default
def set_package_status(package, truck, time):
    if package.delivery_time <= time:
        package.package_status = 'delivered'
    elif package.delivery_time > time < truck.hub_departure:
        var = None
    else:
        package.package_status = 'en route'
