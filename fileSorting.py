from time import sleep
import os

def bubble_sort(file):
    file = list(file.items())
    loop = True
    while loop:
        loop = False
        for i in range(len(file)-1):
            if(file[i][1] > file[i+1][1]):
                file[i], file[i+1] = file[i+1], file[i]
                loop = True

def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p-1)
        quicksort(A, p+1, hi)

def partition(A, lo, hi):    
    pivot = A[hi][1]
    i = lo
    for j in range(lo,hi):
        if A[j][1] < pivot:
            A[i], A[j] = A[j], A[i]
            update((i, j))
            i += 1
    A[i], A[hi] = A[hi], A[i]
    return i

path = os.path.abspath("hunspell-french-dictionaries-v7.0")
filename = "fr-classique.dic"

with open(os.path.join(path,filename),'rb') as f:
    file = {}
    for line in f.readlines():
        word = line.split(b"/")[0]
        file[word] = len(word)

bubble_sort(file)
# quicksort(list(file.items()), 0, len(file)-1)

with open(os.path.join(path,'fr-classique-words.txt'),'wb') as f:
    for word in file:
        f.write(word)
        f.write(b"\n")
print("Done!")
