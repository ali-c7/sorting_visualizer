import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

random.seed('ABC')

amount = 20

numbers = [random.randint(0, 1000) for _ in range(amount)]


def merge(L1, L2, L, L_original):
    pos1 = 0
    pos2 = 0
    posL = 0
    while (pos1 < len(L1)) and (pos2 < len(L2)):
        if L1[pos1] < L2[pos2]:
            L[posL] = L1[pos1]
            L_original[posL] = L1[pos1]
            pos1 += 1
        else:
            L[posL] = L2[pos2]
            L_original[posL] = L2[pos2]
            pos2 += 1
        posL += 1
    while (pos1 < len(L1)):
        L[posL] = L1[pos1]
        L_original[posL] = L[posL]
        pos1 = pos1 + 1
        posL = posL + 1
    while (pos2 < len(L2)):
        L[posL] = L2[pos2]
        L_original[posL] = L[posL]
        pos2 = pos2 + 1
        posL = posL + 1


def merge_sort(L_original, L):

    if len(L) >= 2:
        mid = len(L) // 2
        L1 = L[:mid]
        L2 = L[mid:]
        #print(L_original)
        #print(L)
        merge_sort(L_original, L1)
        merge_sort(L_original, L2)

        merge(L1, L2, L, L_original)
    #print(L_original)

lst = [8, 5, 2, 4, 3, 1, 9, 6]

x = np.arange(0, len(lst), 1)

plt.bar(x, lst)
merge_sort(lst, lst)

plt.show()