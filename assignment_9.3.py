def make_myset(capacity, hash_func= hash):

    table = [[] for _ in range(capacity)]

    return (hash_func, table)



def add(myset, element):

    has_func = myset[0]
    table = myset[1]

    capacity = len(table)

    index = has_func(element) % capacity

    row = table[index]

    for entry in row:

        if entry == element:
            return

    table[index].append(element)

def hash_bad(a_string):
    total = 0

    for char in a_string:

        total += ord(char)
    
    return total

def hash_good(a_string):

    total = 0
    for char in range(a_string):
        total += ord(a_string)*31**(len(a_string)-char+1)
    
    return total



def quality_hash_function(myset):
    total = 0
    for list in myset[1]:
        if len(list) == 1:
            total += 1
    return total
    




