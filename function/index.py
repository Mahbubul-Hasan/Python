def sum(arg1, arg2):
    if type(arg1) != type(arg2):
        print("Type doesn't match")
        return
    print(arg1 + arg2)


sum(15, 60)
sum(15.6, 60.2)
sum("Hello", " Word")
sum("hello", 15)
