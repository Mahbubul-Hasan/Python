D = {
    "name": "Max",
    "age": 32,
    "year": 1988
}
E = {
    "name": "Tom",
    10: 10,
    15.01: 15.01,
    True: True,
    (2, 3): 5
}
print(D)

print(E)
print(E[(2, 3)])

print(len(D))

print(D["name"])
print(D.get("name"))

D["Surname"] = "Tesar"
print(D)

D["name"] = "Tom"
print(D)

D.update({"name": "Tom"})
print(D)

D.pop("year")
D.popitem()
print(D)

print(D.keys())
print(D.values())
print(D.items())

E.clear()
print(E)

del E
print(E)
