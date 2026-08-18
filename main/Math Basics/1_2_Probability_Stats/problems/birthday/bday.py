import matplotlib.pyplot as plt
plt.style.use("dark_background")

def factorial(x):
    res = 1
    while x:
        res*=x
        x-=1
    return res

def p_no_match(k):
    ways = factorial(365)/(factorial(365-k))
    return ways/365**k
    
def p_at_least_one_match(k):
    return 1 - p_no_match(k)

x = [x for x in range(1,100)]
y = [p_at_least_one_match(k) for k in x]

plt.scatter(x,y)
plt.show()

