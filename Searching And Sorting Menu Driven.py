import random

def options():
    print("1 FILL")
    print("2 PRINT")
    print("3 LINEAR SEARCH")
    print("4 BINARY SEARCH")
    print("5 BUBBLE SORT INEFFICIENT")
    print("6 BUBBLE SORT EFFICIENT")
    print("7 INSERTION SORT")
    print("8 QUIT")
    x = int(input("Enter Your Choice : "))
    return x

def filling(item):
    i = 0
    while i < 10:
        temp = random.randint(10,99)
        item[i] = temp
        i = i + 1


def print_array(item):
    a = 0
    while a < 10:
        print(item[a])
        a = a + 1


def linear_search(x,item):
    i = 0
    found = False
    while i < 10 and not(found):
        if item[i] == x:
            found = True
        i = i + 1
    return found


def binary_search(search_item,item):
    max = 9
    min = 0
    while min <= max:
        mid = (max + min) // 2
        if item[mid] == search_item:
            return 1
        else:
            if search_item > item[mid]:
                min = mid + 1
            else:
                max = mid - 1
    return 0


def buuble_sort_inefficient(item):
    max = 9
    while max > 0:
        index = 0
        while index <max:
            if item[index] > item[index+1]:
                temp = item[index]
                item[index] = item[index+1]
                item[index+1] = temp
            index = index+1
        max = max - 1

def bubble_sort_efficient(item):
    max = 9
    swap = True
    while swap == True:
        index = 0
        swap = False
        while index < max:
            if item[index] > item[index + 1]:
                temp = item[index]
                item[index] = item[index + 1]
                item[index + 1] = temp
                swap = True
            index = index + 1
        max = max - 1


def insertion_sort(item):
    max = 0
    while max < 9:
        temp = item[max+1]
        pos = max+1
        while item[pos-1] > temp and pos >0:
            item[pos] = item[pos-1]
            pos = pos-1

        item[pos] = temp
        max = max +1


def main():
    item = [0]*10
    choice = 0
    while choice != 8:

        choice = options()
        if choice == 1:
            filling(item)

        elif choice == 2:
            print_array(item)

        elif choice == 3:
            search_item_linear = int(input("Enter item you want to search : "))
            check = linear_search(search_item_linear,item)

            if check == True:
                print("FOUND")

            else:
                print("NOT FOUND")

        elif choice == 4:
            search_item_binary = int(input("Enter item you want to search"))
            found = binary_search(search_item_binary,item)
            if found == 1:
                print("FOUND")
            else:
                print("NOT FOUND")

        elif choice == 5:
            buuble_sort_inefficient(item)

        elif choice == 6:
            bubble_sort_efficient(item)

        elif choice == 7:
            insertion_sort(item)

        elif choice == 8:
            print("GOOD BYE")
        else:
            print("INVALID INPUT ! TRY AGAIN")

main()