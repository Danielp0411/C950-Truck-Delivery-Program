#  --------------------------
#  Daniel Phillips #001044985
#  --------------------------
import trucks
from datetime import timedelta, datetime
from csvreader import h

#  starts the truck routes
trucks.nearest_neighbor(trucks.truck1)
trucks.nearest_neighbor(trucks.truck2)
trucks.nearest_neighbor(trucks.truck3)

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
    print('Mileage:\nTruck 1: ' + str(trucks.truck1.miles)
          + '\nTruck 2: ' + str(trucks.truck2.miles) + '\nTruck 3: ' + str(trucks.truck3.miles)
          + '\nTotal mileage: ' + str(trucks.truck1.miles + trucks.truck2.miles + trucks.truck3.miles))
#  prints package information by the user-entered package ID
elif user_selection == '2':
    ID = input('Enter package ID: ')
    print('Package ID: ' + (h.lookup(ID)).package_id)
    print('Delivery Address: ' + (h.lookup(ID)).package_address)
    print('Delivery Deadline: ' + (h.lookup(ID)).package_delivery_deadline)
    print('Delivery City: ' + (h.lookup(ID)).package_city)
    print('Delivery Zip Code: ' + (h.lookup(ID)).package_zip)
    print('Weight: ' + (h.lookup(ID)).package_weight)
    print('Delivery Status: ' + (h.lookup(ID)).package_status + ' : ' + str((h.lookup(ID)).delivery_time))

#  Rubric: G - prints the status of all packages at a specific time
elif user_selection == '3':
    try:
        time = input("Please type a specific time (format: HH:MM): ")
        t = datetime.strptime(time, '%H:%M')
        delta = timedelta(hours=t.hour, minutes=t.minute)

        i = 1
        while i <= 40:
            if (h.lookup(str(i))).delivery_time < delta:
                print('[ID] ' + (h.lookup(str(i))).package_id + ' [Status] ' + (
                    h.lookup(str(i))).package_status + ' : ' + str((h.lookup(str(i))).delivery_time))
            else:
                print('[ID] ' + (h.lookup(str(i))).package_id + ' [Status] ' + (h.lookup(str(i))).package_status)
            i = i + 1
    except (ValueError, NameError):
        print('Oops! That was not the correct format. Please try again!')

else:
    print('Invalid entry. Please try again.')
