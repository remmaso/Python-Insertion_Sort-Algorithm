# Insertion sort is the simple method of sorting an array. In this technique, the array is virtually split into the sorted and unsorted part. An element from unsorted part is picked and is placed at correct position in the sorted part. The array elements are traversed from 1 to n

## This program defines the insertion_sort function that takes an input list arr and sorts it in ascending order using the Insertion Sort algorithm.

## To run the program, save the code in a file with a .py extension (e.g., insertion_sort.py). Then, open a terminal or command prompt, navigate to the directory where the file is saved, and run the following command:

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
numbers = [5, 2, 8, 12, 3]
print("Original list:", numbers)

insertion_sort(numbers)
print("Sorted list:", numbers)

## The program will execute and display the original list followed by the sorted list.

## In the example provided, the original list is [5, 2, 8, 12, 3], and the output will be:
