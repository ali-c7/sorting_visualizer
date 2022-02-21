import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def swap(L, p1, p2):
    temp = L[p1]
    L[p1] = L[p2]
    L[p2] = temp


def insert(L, pos):
    '''
    Sorts L from 0 to pos inclusive

    Mutates L

    insert: (listof Int) Nat -> None
    Requires: L from 0 to pos-1 is sorted.
    '''
    while pos > 0 and L[pos] < L[pos - 1]:
        swap(L, pos, pos - 1)
        pos = pos - 1


def insertion_sort(x, L):
    for i in range(1, len(L)):
        insert(L, i)
        plt.bar(x, L)
        plt.pause(0.001)
        plt.clf()

amount = 50
lst = np.random.randint(0, 100, amount)
removed_duplicates = []

for i in range(len(lst)):
    if lst[i] not in removed_duplicates:
        removed_duplicates.append(lst[i])

x = np.arange(0, len(removed_duplicates), 1)

insertion_sort(x, removed_duplicates)

plt.bar(x, removed_duplicates)
plt.show()