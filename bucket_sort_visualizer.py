import numpy as np
import matplotlib.pyplot as plt


def bucket_sort(L):

    upper = max(L)
    counts = [0] * (upper + 1)
    m = []
    for k in L:
        counts[k] += 1
    for j in range(len(counts)):
        m += [j] * counts[j]
    for i in range(len(L)):
        L[i] = m[i]
        plt.bar(list(range(len(L))), L)
        plt.pause(.001)
        plt.clf()

amount = 100
lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

print(lst)
bucket_sort(lst)
print(lst)
plt.bar(x, lst)
plt.show()
