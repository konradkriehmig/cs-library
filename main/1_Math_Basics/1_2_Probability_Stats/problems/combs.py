def count_combs(n, k):
    pass

def get_combs(n, k):
    res = []
    cur = []
    def BT(j):
        if len(cur) == k:
            res.append(cur[:])
            return
        for i in range(j, n+1):
            cur.append(i)
            BT(i+1)
            cur.pop()
    BT(1)
    return res

print(get_combs(5, 3))
