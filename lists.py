x = [1, 3, 5, 7, 9]
print(len(x))
x.append(11)
print(len(x))
x.extend([13, 15, 17, 19])
print(len(x))
print(x.pop())
print(len(x))
print(x[1])
x[0] = "Hello"
print(x[0])

y = (2, 4, 6, 8, 10)#tuple #immutable
