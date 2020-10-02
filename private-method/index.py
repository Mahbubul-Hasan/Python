class Hello():

    def public_method(self):
        print("public method")
        self.__private_method()

    def __private_method(self):
        print("private method")


hello = Hello()
hello.public_method()
