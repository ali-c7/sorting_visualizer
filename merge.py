def merge(L1, L2, L, L_original, half):
    i = 0
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
        if posL == len(L_original) // 2:
            i += 1
        #print("posL", posL)

    while (pos1 < len(L1)):
        L[posL] = L1[pos1]

        L_original[posL]= L1[pos1]
        pos1 = pos1 + 1
        posL = posL + 1
        if posL == len(L_original) // 2:
            i += 1

    while (pos2 < len(L2)):
        L[posL] = L2[pos2]
        L_original[posL] = L2[pos2]
        pos2 = pos2 + 1
        posL = posL + 1
        if posL == len(L_original) // 2:
            i += 1

    print(pos1, pos2, posL ,"L", L)
    print(i)
def merge_sort(L, L_original):
    if len(L) >= 2:
        mid = len(L) // 2
        L1 = L[:mid]
        L2 = L[mid:]
        merge_sort(L1, L_original)
        merge_sort(L2, L_original)
        #print(L)
        merge(L1, L2, L, L_original)
        ##print(L)
L = [5, 8, 2, 4, 3, 1, 9, 6]

merge_sort(L, L)
print("L sorted", L)
