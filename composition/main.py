class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def anual_salary(self):
        return (self.pay * 12) + self.bonus



class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age

        self.obj_salary = Salary(pay, bonus)

    def total_salary(self):
            return self.obj_salary.anual_salary()



employee = Employee("Max", 24, 15000, 10000)
print(employee.total_salary())
