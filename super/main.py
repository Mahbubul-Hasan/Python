class Parent():
    def __init__(self):
        print("Parent __init__")

    def name(self, name):
        print("Parent's name is", name)

class Parent2():
    def __init__(self):
        print("Parent2 __init__")

    def name(self, name):
        print("Parent2's name is", name)

# class Child(Parent):
#     def __init__(self):
#         print("Child __init__")
#         super().__init__()
#         super().name("Max")

class Child(Parent, Parent2):
    def __init__(self):
        print("Child __init__")
        Parent.__init__(self)
        Parent2.name(self, "Max")

child = Child();
