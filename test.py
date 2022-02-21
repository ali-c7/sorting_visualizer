import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

amount = 15

lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

n = len(lst)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect(1)

for i in range(n):
    for j in range(0, n-i-1):
        plt.bar(x, lst)
        plt.pause(0.01)
        plt.clf()
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

st.pyplot(fig)