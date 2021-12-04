"""
A hash function is a function that maps a key "X" to a whole number in a fixed range"""


def hash1(x):
    return (x**2 - 6*x + 9)%10

print(hash1(4))


def string_hash(x: str):
    s = 0
    for char in x:
        s = s + ord(char)
    return s % 50

print(string_hash('samuel'))


