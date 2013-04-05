
def swap_k(L, k):
# indexing error
    if k>len(L)//2 or k<=0:
        L=L
    else:
        swapped_list = []
        swapped_list.extend(L[-k:])
        swapped_list.extend(L[k+1:-k-1])
        swapped_list.extend(L[:k])
        L.clear()
        L.extend(swapped_list)

def bug_swapk2(L, k):
    # return, though shouldn't
    if k>len(L)//2 or k<=0:
        L=L
    else:
        swapped_list = []
        swapped_list.extend(L[-k:])
        swapped_list.extend(L[k:-k])
        swapped_list.extend(L[:k])
        L.clear()
        L.extend(swapped_list)
    return L

def bug_swapk3(L, k):

        tmp_beg, tmp_end = [], []
        for i in range(k):
            tmp_end.append(L.pop())
            tmp_beg.append(L.pop(0))
        for i in range(k):
            L.append(tmp_beg.pop())
            L.insert(0, tmp_end.pop())
