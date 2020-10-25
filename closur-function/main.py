def nth_power(exponent):
    def pow_of(base):
        print(pow(base, exponent))
    return pow_of

square = nth_power(2)
square(2)
square(3)
square(4)