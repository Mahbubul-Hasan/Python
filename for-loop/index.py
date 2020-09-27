for i in range(0, 5):
    print(i)
else:
    print("End loop")

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
B = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
C = set((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
d = "0123456789"
e = {
    "name": "Max",
    "age": 24
}

print(5 in B)

for i in a:
    print(i)

for i in e.values():
    print(i)

for key, value in e.items():
    print(key, "=", value)
