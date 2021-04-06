#  --------------------------
#  Daniel Phillips #001044985
#  --------------------------
from trucks import *
from datetime import timedelta, datetime
from csvreader import h
from utils import ANSICodes

#  prints user interface title and options
print('----------Western Governors University Parcel Service----------')
print('Choose from the options below:')
user_selection = input("0: exit the program\n"
                       "1: lookup truck mileage\n"
                       "2: lookup package by ID\n"
                       "3: lookup package statuses by time\n")

#  exits application if user types 0
if user_selection == '0':
    exit()

#  prints the mileage of each truck and the total mileages of all trucks
elif user_selection == '1':
    start_routes(timedelta(hours=-0))
    print('Mileage:\nTruck 1: ' + str(round(truck1.miles, 2))
          + '\nTruck 2: ' + str(truck2.miles) + '\nTruck 3: ' + str(truck3.miles)
          + '\nTotal mileage: ' + str(round(truck1.miles + truck2.miles + truck3.miles, 2)))

#  prints package information by the user-entered package ID
elif user_selection == '2':
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
        time = input("Please type a specific time (format: HH:MM): ")
        t = datetime.strptime(time, '%H:%M')
        delta = timedelta(hours=t.hour, minutes=t.minute)
        start_routes(delta)
        i = 1
        while i <= 40:
            package = h.lookup(str(i))
            if package.package_status == 'delivered':
                print(
                    '[ID]  ' + package.package_id + '     [Address]  ' + package.package_address + '     [Deadline]  '
                    + package.package_delivery_deadline + '     [City]  ' + package.package_city + '     [Zip Code]  '
                    + package.package_zip + '     [Weight]  ' + package.package_weight + '     [Status]  '
                    + ANSICodes.green(package.package_status) + ' @ ' + str(package.delivery_time))
            elif package.package_status == 'en route':
                print(
                    '[ID]  ' + package.package_id + '     [Address]  ' + package.package_address + '     [Deadline]  '
                    + package.package_delivery_deadline + '     [City]  ' + package.package_city + '     [Zip Code]  '
                    + package.package_zip + '     [Weight]  ' + package.package_weight + '     [Status]  '
                    + ANSICodes.cyan(package.package_status))
            else:
                print(
                    '[ID]  ' + package.package_id + '     [Address]  ' + package.package_address + '     [Deadline]  '
                    + package.package_delivery_deadline + '     [City]  ' + package.package_city + '     [Zip Code]  '
                    + package.package_zip + '     [Weight]  ' + package.package_weight + '     [Status]  '
                    + ANSICodes.yellow(package.package_status))
            i = i + 1
    except (ValueError, NameError):
        print('Oops! That was not the correct format. Please try again!')

else:
    print('Invalid entry. Please try again.')
