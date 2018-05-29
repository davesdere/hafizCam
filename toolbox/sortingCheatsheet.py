#### @Davesdere | David Cote | MIT License 2018
# coding: utf-8
# 16/02/2018
# Let's compare algorithms

print('# # # # # # # # # # # # # # # # # # # # #')
print('Algorithme          Best Case     Worst Case')
print('Tri par selection : O(n^2)        O(n^2)')
print('Tri par insertion : O(n)          O(n^2)')
print('Tri a bulle       : O(n^2)        O(n^2)')
print('Tri par fusion    : O(n log n)    O(n log n)')
print('Tri rapide        : O(n log n)    O(n^2)')
print('# # # # # # # # # # # # # # # # # # # # #')

# # # # # # # # # # # # # # # # # # # # # # #
# The Selection Sort
# The best case scenario : O(n^2)
# The worst case scenario : O(n^2)
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
print('# # # # # # # # # # # # # # # # # # # # #')
print('#     Selection Sort')
print('Random Numbers ->')
aList = [54,26,93,17,77,31,44,55,20]
print(*aList)
selectionSort(aList)
print('Sorted list ->')
print(*aList)

# # # # # # # # # # # # # # # # # # # # # # #
# Insertion Sort
# The best case scenario : O(n)
# The worst case scenario : O(n^2)
# Complexity level: O(n^2)
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
# The result
print('# # # # # # # # # # # # # # # # # # # # #')
print('#     Insertion Sort')
print('Random Numbers ->')
blist = [2,126,93,1,77,31,44,55,20]
print(*blist)
insertionSort(blist)
print('Sorted list ->')
print(*blist)


# # # # # # # # # # # # # # # # # # # # # # #
# Bubble Sort
# The best case scenario : O(n^2)
# The worst case scenario : O(n^2)
# T(n) = ?
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
# The result
print('# # # # # # # # # # # # # # # # # # # # #')
print('#    Bubble Sort')
print('Random Numbers ->')
clist = [54,26,93,17,77,31,44,55,20]
print(*clist)
bubbleSort(clist)
print('Sorted list ->')
print(*clist)

# # # # # # # # # # # # # # # # # # # # # # #
# The Merge Sort
# The best case scenario : O(n log n)
# The worst case scenario : O(n log n)
# T(n) = O(n log n)
# Merge sort uses recursion to divide and conquer
# Uncomment the print to see the algorithm working
def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

# The result
print('# # # # # # # # # # # # # # # # # # # # #')
print('#     Merge Sort')
print('Random Numbers ->')
elist = [54,26,93,17,77,31,44,55,20]
print(*elist)
mergeSort(elist)
print('Sorted list ->')
print(*elist)

# # # # # # # # # # # # # # # # # # # # # # #
# Quick Sort
# The best case scenario : O(n log n)
# The worst case scenario : O(n^2)
# T(n) = O(n log n)
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

# The result
print('# # # # # # # # # # # # # # # # # # # # #')
print('#    Quick Sort')
print('Random Numbers ->')
dlist = [54,26,93,17,77,31,44,55,20]
print(*dlist)
quickSort(dlist)
print('Sorted list ->')
print(*dlist)

# Let's compare algorithms
print('Algorithme          Best Case     Worst Case')
print('Tri par selection : O(n^2)        O(n^2)')
print('Tri par insertion : O(n)          O(n^2)')
print('Tri a bulle       : O(n^2)        O(n^2)')
print('Tri par fusion    : O(n log n)    O(n log n)')
print('Tri rapide        : O(n log n)    O(n^2)')

# # # # # # # # # # # # # # # # # # # # # # #
#That was the implementation based on textbook which doesn't work.
# Selection Sort
# It swaps items
# Complexity level: O(n^2)

# randomNumbers = [12, 23, 2, 1, 3, 4, 5, 6]
# def selectionSort(list):
    # sortedList = []
    # print(*list)
    # print(*list, sep= ' -> ')
    # original = list
    # for i in range(len(list)):
        # indMin = i
        # for j in range(len(list)):
            # if list[j] < list[indMin]:
                # indMin = j
                # print(j, '= j < i = ', i)
    # if indMin > i:
        # print(indMin, ' > ', i)
        # tmp = list[i]
        # list[i] = list[indMin]
        # list[j] = tmp
        
    # return sortedList
# # The list looks like:
# print(selectionSort(randomNumbers))
# print(randomNumbers)
