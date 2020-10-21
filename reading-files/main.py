fileHandling = open("reading-files/test.txt", "r")

# print(fileHandling.read())
# print(fileHandling.read(4))
# ------------------------
# print(fileHandling.readline())
# print(fileHandling.readline())
# print(fileHandling.readline())
# ------------------------
# print(fileHandling.readlines())
# print(fileHandling.readlines()[3])

for list in fileHandling:
    # print(list)
    # print(len(list))
    # print(list.split(" "))
    print(len(list.split(" ")))


fileHandling.close()
