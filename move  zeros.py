def move_zeros(lst):
    return sorted(lst, key=lambda x: x == 0 and type(x) is not bool)

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
