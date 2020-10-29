class Tab():
    
    menu = {
        'wine': 5,
        'beer': 3,
        'soft drink': 2,
        'chicken': 10,
        'beef': 15,
        'veggie': 12,
        'desert': 6,
    }

    def __init__(self):
        self.items = []
        self.total = 0
        self.tex = 0
        self.service = 0

    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    def print_bill(self):
        self.tex = 15/100 * self.total
        self.service = 10 / 100 * self.total
        self.total = self.total + self.tex + self.service
        
        for item in self.items:
            print(f'{item.capitalize():35} = ${self.menu[item]:.2f}')

        print(f"{'Total bill including tex & service':35} = ${self.total:.2f}")
