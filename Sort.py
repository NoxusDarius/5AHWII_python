import random
import copy
import time


def bubble_sort(unsorted_list):
    end = len(unsorted_list)
    for i in range(end):
        # -1 weil wir immer mit dem nachfolger element tauschen aber das letzte element keinen nachfolger hat
        for j in range(0, end-1-i):
            if unsorted_list[j] > unsorted_list[j+1]:
                # In Python kann man die Zahlen direkt wechseln mann braucht keine cache (Zwischenvariable) dafür
                # beide operationen werden gleichzeitig ausgeführt
                unsorted_list[j], unsorted_list[j +
                                                1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list


def insertion_sort(unsorted_list):
    # Aufwandsklasse n^2
    sorted_list = []
    while(len(unsorted_list) > 0):
        smallest = unsorted_list[0]
        smallest_index = 0
        # enumerate speichert zusätzlich no den index mit ab
        for index, element in enumerate(unsorted_list):
            if element < smallest:
                smallest = element
                smallest_index = index
                # The pop() method removes the item at the given index from the list and returns the removed item
        unsorted_list.pop(smallest_index)
        sorted_list.append(smallest)
    return sorted_list


def selection_sort(unsorted_list):
    # ist ein inplace verfahren
    for index in range(len(unsorted_list)):
        min_index = index

        for i in range(min_index+1, len(unsorted_list)):
            if unsorted_list[min_index] > unsorted_list[i]:
                min_index = i
        unsorted_list[index], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[index]

    return unsorted_list


if __name__ == "__main__":
    l = []

    for i in range(999):
        # append befüllt die Liste
        # the radiant method() returns an integer number from the specified range
        l.append(random.randint(0, 999))
    c, b = copy.deepcopy(l), copy.deepcopy(l)
    print(l, b, c)
    #print("Hier die Zahlen von L:"+str(l)+"Hier das ende der Zahlen l")
    start = time.time()
    l = bubble_sort(l)
    end = time.time()
    print("\nHier ist l" + str(l) +
          " \n Hier ist die Zeit von Bubblesort: " + str(end-start))

    start2 = time.time()
    c = insertion_sort(c)
    end2 = time.time()
    print("\n Hier ist c" + str(c) +
          "\n Hier ist die Zeit von Insertionsort: " + str(end2-start2))

    start3 = time.time()
    b = selection_sort(b)
    end3 = time.time()
    print("\nHier ist b" + str(b) +
          "\n Hier ist die Zeit von selectionsort: " + str(end3-start3))
    print("HALLO")
