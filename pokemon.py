import csv
import random

def make_database(filename):
    database = []

    with open(filename, 'r') as data:
      
        for line in csv.DictReader(data):
            database.append(line)
    return database
def make_pack(filename):
    pack = []
    database = make_database(filename)
    
    for i in range(10):
        rand = random.randint(0, len(database))
        pack.append(database.pop(rand))
    return pack


def build_basic_database(function):
    collection = []
    function = make_pack()
    count = 0

    for i in range(len(function)):
        collection.append(function[i])
        count += 1
    return count
    
def build_counting_collection(function):
    function = make_pack()
def main():

    # make_database("data/pokemon.csv")
    # print(make_database)
    print(make_pack("data/pokemon.csv"))

main()