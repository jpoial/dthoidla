#!/usr/bin/env python3

import time
import random
import sys


def main():
    n = 4000
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    t_2 = time.perf_counter()
    a = []
    for i in range(n):
        a.append(random.randint(0, 999))
    copy1 = list(a)
    copy2 = list(a)
    copy3 = list(a)
    copy4 = list(a)
    copy5 = list(a)
    copy6 = list(a)
    copy7 = list(a)
    t_1 = time.perf_counter()
    print("List generation time: " + str(int(1000. * (t_1 - t_2))) + " ms")
    print("Len: " + str(len(copy1)))
    t0 = time.perf_counter()
    quicksort(copy1, 0, len(copy1))
    t1 = time.perf_counter()
    mergesort(copy2, 0, len(copy2))
    t2 = time.perf_counter()
    selectionsort(copy3)
    t3 = time.perf_counter()
    binsertionsort(copy4)
    t4 = time.perf_counter()
    insertionsort(copy5)
    t5 = time.perf_counter()
    bubblesort(copy6)
    t6 = time.perf_counter()
    copy7.sort()
    t7 = time.perf_counter()
    print("Time quicksort: " + str(int(1000. * (t1 - t0))) + ' ms')
    checkorder(copy1)
    print("Time mergesort: " + str(int(1000. * (t2 - t1))) + ' ms')
    checkorder(copy2)
    print("Time selecsort: " + str(int(1000. * (t3 - t2))) + ' ms')
    checkorder(copy3)
    print("Time binsrsort: " + str(int(1000. * (t4 - t3))) + ' ms')
    checkorder(copy4)
    print("Time insertsrt: " + str(int(1000. * (t5 - t4))) + ' ms')
    checkorder(copy5)
    print("Time bubblesrt: " + str(int(1000. * (t6 - t5))) + ' ms')
    checkorder(copy6)
    print("Time systemsrt: " + str(int(1000. * (t7 - t6))) + ' ms')
    checkorder(copy7)
    if copy1 == copy2 and copy2 == copy3 and copy3 == copy4 and \
            copy4 == copy5 and copy5 == copy6 and copy6 == copy7:
        print("ok")


def checkorder(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            raise ValueError("Wrong order: " + str(arr[i]) + " > " +
                             str(arr[i+1]) + " index " + str(i))


def insertionsort(arr):
    if len(arr) < 2:
        return
    for i in range(1, len(arr)):
        b = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] <= b:
                break
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = b


def binsertionsort(arr):
    if len(arr) < 2:
        return
    for i in range(1, len(arr)):
        b = arr[i]
        left = 0
        right = i
        while left < right:
            mid = int((left + right) / 2)
            if b < arr[mid]:
                right = mid
            else:
                left = mid + 1
        arr[left+1:i+1] = arr[left:i]
        arr[left] = b


def quicksort(arr, left, right):
    if (right - left) < 2:
        return
    x = arr[int((left + right) / 2)]
    i = left
    j = right - 1
    while i < j:
        while arr[i] < x:
            i += 1
        while arr[j] > x:
            j -= 1
        if i > j:
            break
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i += 1
        j -= 1
    if left < j:
        quicksort(arr, left, j + 1)
    if i < right - 1:
        quicksort(arr, i, right)


def mergesort(arr, left, right):
    if len(arr) < 2 or (right - left) < 2:
        return
    k = int((left + right)/2)
    mergesort(arr, left, k)
    mergesort(arr, k, right)
    merge(arr, left, k, right)


def merge(arr, left, k, right):
    if len(arr) < 2 or (right - left) < 2 or k <= left or k >= right:
        return
    tmp = [0] * (right - left)
    n1 = left
    n2 = k
    m = 0
    while True:
        if n1 < k and n2 < right:
            if arr[n1] > arr[n2]:
                tmp[m] = arr[n2]
                n2 += 1
            else:
                tmp[m] = arr[n1]
                n1 += 1
            m += 1
        else:
            if n1 >= k:
                tmp[m:] = arr[n2:right]
            else:
                tmp[m:] = arr[n1:k]
            break
    arr[left:right] = tmp[:]


def bubblesort(arr):
    if len(arr) < 2:
        return
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                unsorted = True
                tmp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = tmp


def selectionsort(arr):
    if len(arr) < 2:
        return
    for m in range(0, len(arr) - 1):
        minind = m
        minel = arr[m]
        for i in range(m+1, len(arr)):
            if arr[i] < arr[minind]:
                minind = i
                minel = arr[i]
        arr[m+1:minind+1] = arr[m:minind]
        arr[m] = minel


if __name__ == '__main__':
    main()
