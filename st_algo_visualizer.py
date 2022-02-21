import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib

# Selection sort
def swap(L, p1, p2):
    temp = L[p1]
    L[p1] = L[p2]
    L[p2] = temp


def find_minimum_pos(L, i):
    minimum = min(L[i:])
    result = np.where(L == minimum)
    return result[0][0]
    #return L.index(min(L[i:]), i)


def selection_sort(x, L):
    n = len(L)
    positions = list(range(n - 1))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect(1)
    print("function ran")
    plt.bar(x,L)
    for i in positions:
        print(i)

        plt.bar(x, L)
        plt.pause(0.001)

        min_pos = find_minimum_pos(L, i)
        swap(L, i, min_pos)
        plt.clf()

    plt.bar(x, L)
    st.pyplot(fig)
# User-Interface
st.title("Algorithm Visualizer")

# Functionality


amount = 10
lst = np.random.randint(0, 100, amount)
removed_duplicates = []

for i in range(len(lst)):
    if lst[i] not in removed_duplicates:
        removed_duplicates.append(lst[i])

x = np.arange(0, len(removed_duplicates), 1)

button = st.button("click")
if button:
    selection_sort(x, removed_duplicates)


#plt.show()
