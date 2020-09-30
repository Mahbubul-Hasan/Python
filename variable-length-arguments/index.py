def student(name="Unknown", age=20, *marks):
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)


student("Max", 24, 85, 74, 83, 75)
student()


def student(name="Unknown", age=20, **marks):
    print("Name:", name)
    print("Age:", age)
    print("Marks:--------------")
    for key, value in marks.items():
        print(key.capitalize(), ":", value)


student("Max", 24, english=85, math=74, physics=83, biology=75)
