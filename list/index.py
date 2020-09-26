x = [3, 7, 1, 3, 5, 8, 2, 10]

y = ["Max", 13.1, 5, [3, 2]]

print(x[4])
print(y[3][1])

print(len(x))
print(len(y))

print(x.index(1))

x.insert(3, "Max")
print(x)

x.remove("Max")
print(x)

x.pop()
x.pop(5)
print(x)

x.sort()
print(x)

x.reverse()
print(x)

x.append(15)
print(x)

print(x.count(3))

z = x.copy()
print(z)

y.clear()
print(y)
