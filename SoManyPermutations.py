import itertools


def permutations(s):
    perm_set = itertools.permutations(s)
    return list(set([('').join(list(i)) for i in perm_set]))


print(permutations('aabb'))
