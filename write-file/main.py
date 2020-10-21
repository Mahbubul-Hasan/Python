fileHandling = open('write-file/test.txt', 'a')

try:
    for i in range(10):
        fileHandling.write("This is line number %d\n" %(i+1))
finally:
    fileHandling.close()