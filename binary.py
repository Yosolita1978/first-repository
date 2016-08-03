""" This is an example fuction for binary search"""

def binary_search(list_items, item):
    low = 0
    high = len(list_items)-1

    while low <= high:
        mid = (low + high)
        guess = list_items[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,2,3,4,5,6,7,8,9]

print binary_search(my_list, 5)
print binary_search(my_list, -2)

""" This is an example fuction for sort a list (just to see how it works the sorted fuction)"""

def find_smallest(array):
    smallest_indx = array[0]
    smallest_value = 0
    for i in range(1, len(array)):
        if array[i] < smallest_indx:
            smallest_indx = array[i]
            smallest_value = i
    return smallest_value

def selection_sort(array):
    new_list = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_list.append(array.pop(smallest))
    return new_list

print selection_sort([5, 3, 6, 2, 10])    

