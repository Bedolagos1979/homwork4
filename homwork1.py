a = {'a': 1,
     'b': 2,
     'c': 3}
y = {v: a for a, v in a.items()}
print(y)
