import csv
from packages import Package
from hashtable import HashTable

h = HashTable()  # creates new HashTable object

# Complexity - O(n)
# imports package data from csv file, creates package objects, and adds them to a hash table.
with open('Supporting Docs/packages.csv') as packages_file:
    readCSV = csv.reader(packages_file, delimiter=',')
    for row in readCSV:
        package_id = row[0]
        package_address = row[1]
        package_city = row[2]
        package_state = row[3]
        package_zip = row[4]
        package_delivery_deadline = row[5]
        package_weight = row[6]
        package_note = row[7]

        #  changes package #9 to the corrected address
        if package_id == '9':
            package_address = '410 S State St'
            package_zip = '84111'

        #  creates a package object for each package
        p1 = Package(package_id, package_address, package_city, package_state, package_zip, package_delivery_deadline,
                     package_weight, package_note, 'at the hub', '')

        #  places each package into the hash table with their package ID as the key
        h.insert(package_id, p1)

# Complexity - O(n)
# imports distance data from csv file.
with open('Supporting Docs/distances.csv') as distances_file:
    distance_data = []
    readCSV = csv.reader(distances_file, delimiter=',')
    for row in readCSV:
        distance_data.append(row)

# Complexity - O(n)
# imports address data from csv file.
with open('Supporting Docs/addresses.csv') as addresses_file:
    address_data = []
    readCSV = csv.reader(addresses_file, delimiter=',')
    for row in readCSV:
        address_data.append(row)


# Complexity - O(n)
# returns a numeric value that represents the location of the address entered.
def address_lookup(address):
    i = 0
    while i < len(address_data):
        if address == address_data[i][1]:
            return i
        else:
            i = i + 1
