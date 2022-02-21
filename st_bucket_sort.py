import streamlit as st
import pandas as pd
import numpy as np
import time



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
        time.sleep(0.1)

i = 0

amount = 50
lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

ans = st.button("Click to visualize")
if ans:
    bucket_sort(lst)
