import time

def in_place_reverse(a_list):
    a_list = []
    while a_list:
        a_list.insert(len(a_list), a_list.pop())

        print(a_list)
        break
def my_slice(a_list,start,stop,step=1):
    
    
    
    list = a_list[start:stop:step]
    
    list = [0,10,20,30,40,50]

    print(list)

def make_multiplication_table(number):
    for i in range(number):
        print(*[j*i for j in range(number)], sep="\t")

    



def main():
    """
    a_lis = [1, 2, 3, 4, 5, 6]

    in_place_reverse(a_lis)"""

    a_list=[]
    my_slice(a_list,2,4)

    make_multiplication_table(10)

main()