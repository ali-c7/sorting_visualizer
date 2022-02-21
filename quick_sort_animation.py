import streamlit as st
import matplotlib.pyplot as plt
import numpy as np



def quick_sort(L):
    if len(L) in [0, 1]:
        return L

    x = L[0]
    L1 = list(filter(lambda y: y <= x, L))
    L2 = list(filter(lambda z: z > x, L))
    L1.pop(0)
    quick_sort(L1)
    quick_sort(L2)
    L = L1 + [x] + L2
    print(L)
    return L

L = [5, 2, 3, 8, 1]
quick_sort(L)
print(L)