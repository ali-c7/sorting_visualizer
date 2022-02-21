import streamlit as st
import pandas as pd
import numpy as np
import time


# Bucket sort
def bucket_sort(L):
    chart = st.empty()
    upper = max(L)
    counts = [0] * (upper + 1)
    m = []
    for k in L:
        counts[k] += 1
    for j in range(len(counts)):
        m += [j] * counts[j]
    for i in range(len(L)):
        L[i] = m[i]
        chart_data = pd.DataFrame(L, columns=["a"])
        chart.bar_chart(chart_data)
        time.sleep(0.09)


# Selection sort
def swap(L, p1, p2):
    temp = L[p1]
    L[p1] = L[p2]
    L[p2] = temp


def find_minimum_pos(L, i, order):
    if order == 1:
        minimum = min(L[i:])
        result = np.where(L == minimum)
        return result[0][0]
    else:
        maximum = max(L[i:])
        result = np.where(L == maximum)
        #return L.index(min(L[i:]), i)


def selection_sort(x, L, order):
    chart = st.empty()
    n = len(L)
    positions = list(range(n - 1))

    for i in positions:
        #chart_data = pd.DataFrame(L, columns=["a"])
        #chart.bar_chart(chart_data)
        #time.sleep(0.1)
        min_pos = find_minimum_pos(L, i, order)
        swap(L, i, min_pos)

        chart_data = pd.DataFrame(L, columns=["value"])
        chart.bar_chart(chart_data)
        time.sleep(0.09)


# Insertion sort
def swap(L, p1, p2):
    temp = L[p1]
    L[p1] = L[p2]
    L[p2] = temp


def insert(L, pos, order):
    '''
    Sorts L from 0 to pos inclusive

    Mutates L

    insert: (listof Int) Nat -> None
    Requires: L from 0 to pos-1 is sorted.
    '''
    if order == 1:
        while pos > 0 and L[pos] < L[pos - 1]:
            swap(L, pos, pos - 1)
            pos = pos - 1
    else:
        while pos > 0 and L[pos] > L[pos - 1]:
            swap(L, pos, pos - 1)
            pos = pos - 1

def insertion_sort(x, L, order):
    chart = st.empty()
    for i in range(1, len(L)):
        insert(L, i, order)
        chart_data = pd.DataFrame(L, columns=["value"])
        chart.bar_chart(chart_data)
        time.sleep(0.09)


# Merge sort
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
        #print("posL", posL)
    while (pos1 < len(L1)):
        L[posL] = L1[pos1]
        L_original[posL]= L1[pos1]
        pos1 = pos1 + 1
        posL = posL + 1
    while (pos2 < len(L2)):
        L[posL] = L2[pos2]
        L_original[posL] = L2[pos2]
        pos2 = pos2 + 1
        posL = posL + 1

    #print(L)

def merge_sort(x, L, L_original):

    if len(L) >= 2:
        mid = len(L) // 2
        chart_data = pd.DataFrame(L_original, columns=["value"])
        chart.bar_chart(chart_data)
        L1 = L[:mid]
        L2 = L[mid:]


        merge_sort(x, L1, L_original)
        merge_sort(x, L2, L_original)
        chart_data = pd.DataFrame(L_original, columns=["value"])
        chart.bar_chart(chart_data)

        merge(L1, L2, L, L_original)
        chart_data = pd.DataFrame(L_original, columns=["value"])
        chart.bar_chart(chart_data)
        time.sleep(0.2)

# User Interface
st.title("Sorting Algorithm Visualizer")
st.write("Prepared by Muhammad Nuh Ali Chaudhry")
st.write("Candidate for BASc. in Structural Engineering and Computer Science Minor")


# Create a sample list


st.header("Generate random data")


col1, col2, col3 = st.columns(3)
with col1:
    amount = int(st.number_input("Enter the amount of integers to sort:", value = 50))
with col2:
    st.empty()


chart = st.empty()
lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)
removed_duplicates = []


for i in range(len(lst)):
    if lst[i] not in removed_duplicates:
        removed_duplicates.append(lst[i])

chart_data = pd.DataFrame(lst, columns=["value"])
chart.bar_chart(chart_data)

col3, col4, col5 = st.columns(3)
with col3:
    algorithm = st.selectbox("Sort using", ("Select", "Bucket Sort", "Insertion Sort", "Selection Sort", "Merge Sort"))
with col4:
    order = st.selectbox("Order of sorting", ("Select", "Ascending"))
with col5:
    st.text("Ready?")
    start = st.button("Sort")

if start:
    if algorithm == "Insertion Sort" :
        st.header("The Insertion Sort Algorithm")
        if order == "Ascending":
            insertion_sort(x, removed_duplicates, 1)
        #else:
        #    insertion_sort(x, removed_duplicates, 0)

    elif algorithm == "Selection Sort":
        st.header("The Selection Sort Algorithm")
        if order == "Ascending":
            selection_sort(x, removed_duplicates, 1)
        #else:
        #    selection_sort(x, removed_duplicates, 0)
    elif algorithm == "Bucket Sort":
        st.header("The Bucket Sort Algorithm")
        bucket_sort(lst)
    elif algorithm == "Merge Sort":
        st.header("The Merge Sort Algorithm")
        chart = st.empty()
        merge_sort(x, removed_duplicates, removed_duplicates)
