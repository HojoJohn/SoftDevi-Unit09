import arrays, time, random, math

def unique_array(an_array, value):

    for index in range(len(an_array)):
        current = an_array[index]

        if current == None:
            an_array[index] = value
            break
            
        elif current == value:
            return

def unique_list(a_list, value):

    length = len(a_list)
    for index in range(length):
        if a_list[index] == value:
            return
    
    a_list.append(value)

def fill_list(length):
    a_list =[]
    start = time.perf_counter()
    for value in range(length):
        unique_list(a_list, value)

    return round(time.perf_counter() - start, 4)

def fill_array(length):
    an_array = arrays.Array(length, None)
    start = time.perf_counter()
    for value in range(length):
        unique_array(an_array, value)
    
    return round(time.perf_counter()-start, 3)

def sets():
    a_set = {1,5,7,9}
    print(a_set)
    a_set.add(10)
    a_set.add(11)
    a_set.add(99)

    for value in a_set:
        print(value, end=" ")
    print()

    b_set=set("abcddcbaabcde")
    print(b_set)
    print()

def unique_set(a_set, value):
    if value not in a_set:
        a_set.add(value)

def fill_set(length):
    a_set= set()
    start= time.perf_counter()
    for value in range(length):
        unique_set(a_set, value)
    return round(time.perf_counter() - start, 6)


def coupon_collector(n):
    collection =set()
    boxes = 0

    while len(collection)< n:
        r = random.randint(1, n)
        collection.add(r)
        boxes +=1
    return boxes
def mixup():
    a_string="abcdefghijklmnopqrstuvxyz"

    a_set =set(a_string)

    for char in a_set:
        print(char, end= " ")
    print()
    print(a_set)

def unique_words(filename):

    a_set = set()

    with open(filename) as file:
        for line in file:
            words=line.split()
            for word in words:
                a_set.add(word.lower())
    return a_set

def superset(a_set, b_set):
    for value in b_set:
        if not(value in a_set):
            return False
    return True

def subset(a_set, b_set):
    for value in a_set:
        if not(value in b_set):
            return False
    
    return True

def intersection(a_set, b_set):
    c_set = set()
    for value in a_set:
        if value in b_set:
            c_set.add(value)
    return c_set

def union(a_set, b_set):
    c_set = set()
    for value in a_set:
        c_set.add(value)
    for value in b_set:
        c_set.add(value)
    return c_set

def minus (a_set, b_set):
    for value in b_set:
        if value in a_set:
            a_set.remove(value)
            
def names():
    names = ()
    names["J"] = "John"
    names["F"] = "Fitz"
    names["K"] = "Kennedy"

    names["J"] = "Jacky"
    print(names["J"])
def print_dict(dictionary):
    for key in dictionary:
        value = dictionary[key]
        print(key)
def main():
    size = 5000
    print("fill array:", fill_array(size), "seconds")
    print("fill array:", fill_list(size), "seconds")

    n = 500000
    boxes = coupon_collector(n)
    print("boxes =", boxes, "theoretical = ", round(n*math.log(n) + 0.577215*n, 0))

    for _ in range(3):
        mixup
    
    filename = "data/alice.txt"
    words = unique_words(filename)
    print("found", len(words), "unique words in", filename)

    a_set = set('abcd')
    b_set = set('cdef')
    c_set = set('ab')
    print("a_set:", a_set)
    print("a_set:", b_set)
    print("a_set:", c_set)

    print("a superset of b?", superset(a_set, b_set))
    print("a superset of c?", superset(a_set, c_set))

    a_dict = {"B":"Buttercup"}

main