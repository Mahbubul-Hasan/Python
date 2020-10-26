for i in range(5):
    print(i)


for i in range(3, 11):
    print(i)

for i in range(0, 21, 4):
    print(i)

burgers = ['beef', 'chicken', 'veg', 'supreme', 'doub']

for i in range(len(burgers)):
    print(f'{i} => {burgers[i]}')

for i in range(len(burgers)-1, -1, -1):
    print(f'{i} => {burgers[i]}')
