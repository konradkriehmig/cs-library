# How many ways are there to choose a two person committee?
def get_two_person_committee_count(n):
    return n * (n - 1) // 2

# Which two person committees can you form from a group of n?
def get_two_person_committees(n):
    return [(i, j) for i in range(1, n) for j in range(i+1, n+1)]

# How many ways are there two split an even group of n into two?

# How can you split up an even group of n into two?
def get_teams(n):
    pass


print(get_two_person_committee_count(5))
print(get_two_person_committees(5))