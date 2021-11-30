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
    pokemon = {}

    while len(pokemon) == 102:
        for  i in range(len(function)):
            pokemon.append(function[i])
    return pokemon


def main():
    print("Cards in database:0", 102)
    # make_database("data/pokemon.csv")
    # print(make_database)
    print("Cards in pack: ")
    print(make_pack("data/pokemon.csv"))

    build_basic_database(make_pack)
    
    build_counting_collection(make_pack)



main()