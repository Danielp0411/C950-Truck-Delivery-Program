#  --------------------------
#  Daniel Phillips #001044985
#  --------------------------
from trucks import *
from datetime import timedelta, datetime
from csvreader import h
from utils import ANSICodes

#  prints user interface title and options
# Complexity - O(1)
print('----------Western Governors University Parcel Service----------')
print('Choose from the options below:')
user_selection = input("0: exit the program\n"
                       "1: lookup truck mileage\n"
                       "2: lookup package by ID\n"
                       "3: lookup package info by time\n")
# Complexity - O(n)
#  exits application if user types 0
if user_selection == '0':
    exit()

#  prints the mileage of each truck and the total mileages of all trucks
elif user_selection == '1':
    # calls the start_routes function to start the trucks on their route.
    start_routes(timedelta(hours=-0))
    print('Mileage:\nTruck 1: ' + str(round(truck1.miles, 2))
          + '\nTruck 2: ' + str(truck2.miles) + '\nTruck 3: ' + str(truck3.miles)
          + '\nTotal mileage: ' + str(round(truck1.miles + truck2.miles + truck3.miles, 2)))

#  prints package information by the user-entered package ID
elif user_selection == '2':
    # calls the start_routes function to start the trucks on their route.
    start_routes(timedelta(hours=-0))
    ID = input('Enter package ID: ')
    print('Package ID: ' + (h.lookup(ID)).package_id)
    print('Delivery Address: ' + (h.lookup(ID)).package_address)
    print('Delivery Deadline: ' + (h.lookup(ID)).package_delivery_deadline)
    print('Delivery City: ' + (h.lookup(ID)).package_city)
    print('Delivery Zip Code: ' + (h.lookup(ID)).package_zip)
    print('Weight: ' + (h.lookup(ID)).package_weight)
    print('Delivery Status: ' + ANSICodes.green((h.lookup(ID)).package_status) + ' : ' + str(
        (h.lookup(ID)).delivery_time))

#  Rubric: G - prints the status of all packages at a specific time
elif user_selection == '3':
    try:
        time = input("Please type a specific time (format: HH:MM), 24hr: ")
        t = datetime.strptime(time, '%H:%M')
        delta = timedelta(hours=t.hour, minutes=t.minute)
        # calls the start_routes function to start the trucks on their route,
        # using the time-entered by user (later used to set the package statuses).
        start_routes(delta)
        print("\n------------------------ALL PACKAGES AS OF " + str(delta) + '------------------------')
        i = 1
        while i <= 40:
            package = h.lookup(str(i))
            if package.package_status == 'delivered':
                print(
                    package.package_id + ' | ' + package.package_address + ' | '
                    + package.package_city + ' | ' + package.package_zip + ' | '
                    + package.package_weight + ' | ' + package.package_delivery_deadline + ' | '
                    + ANSICodes.green(package.package_status) + ' @ ' + str(package.delivery_time))
            elif package.package_status == 'en route':
                print(
                    package.package_id + ' | ' + package.package_address + ' | '
                    + package.package_city + ' | ' + package.package_zip + ' | '
                    + package.package_weight + ' | ' + package.package_delivery_deadline + ' | '
                    + ANSICodes.cyan(package.package_status))
            else:
                print(
                    package.package_id + ' | ' + package.package_address + ' | '
                    + package.package_city + ' | ' + package.package_zip + ' | '
                    + package.package_weight + ' | ' + package.package_delivery_deadline + ' | '
                    + ANSICodes.yellow(package.package_status))
            i = i + 1
    except (ValueError, NameError):
        print('Oops! That was not the correct format. Please try again!')

else:
    print('Invalid entry. Please try again.')