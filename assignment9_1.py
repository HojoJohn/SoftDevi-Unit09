import time


def in_place_reverse(a_list):
    
    # while a_list:
    #     a_list.insert(len(a_list), a_list.pop())

    #     print(a_list)
    length = len(a_list)

    for i in range(int(length/2)):
        temp = a_list.pop(length - i - 1)
        a_list.insert(length - i - 2, a_list.pop(i))
        a_list.insert(i, temp)
    
    print(a_list)
    

def my_slice(a_list,start,stop,step=1):
    list = a_list[start:stop:step]
    
    return list

def make_multiplication_table(number):
    for i in range(number):
        print(*[j*i for j in range(number)], sep="\t")

    



def main():
    
    in_place_reverse([1,2,3,4,5,6, 7])

    
    print(my_slice([0, 10, 20, 30, 40, 50], 5, 1, -1))

    # make_multiplication_table(10)

main()