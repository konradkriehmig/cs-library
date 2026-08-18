def get_digit_right_to_left(num):
    res = []
    while num:
        res.append(num % 10)
        num //= 10
    return res

def get_digit_left_to_right(num):
    res = []
    l = len(str(num))
    for i in range(l-1, -1, -1):
        x = num // (10**i)
        res.append(x)
        num -= x * (10**i)
    return res

# testing
num = 23456
print(get_digit_right_to_left(num))
print(get_digit_left_to_right(num))