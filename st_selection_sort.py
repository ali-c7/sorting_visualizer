import streamlit as st
import pandas as pd
import numpy as np
import time
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
    chart = st.empty()
    n = len(L)
    positions = list(range(n - 1))

    for i in positions:
        #chart_data = pd.DataFrame(L, columns=["a"])
        #chart.bar_chart(chart_data)
        #time.sleep(0.1)
        min_pos = find_minimum_pos(L, i)
        swap(L, i, min_pos)

        chart_data = pd.DataFrame(L, columns=["value"])
        chart.bar_chart(chart_data)
        time.sleep(0.1)

amount = 50
lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)
removed_duplicates = []
for i in range(len(lst)):
    if lst[i] not in removed_duplicates:
        removed_duplicates.append(lst[i])

ans = st.button("Click to visualize")
if ans:
    selection_sort(x, removed_duplicates)
