fileHandling = open('write-file/test.txt', 'a')

try:
    for i in range(10):
        fileHandling.write("This is line number %d\n" % (i+1))
finally:
    fileHandling.close()

# --------------------------------------------------
qoutes = [
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n",
    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n",
    "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n"
]

with open('./write-file/write.txt', 'w') as write_texts:
    write_texts.writelines(qoutes)
