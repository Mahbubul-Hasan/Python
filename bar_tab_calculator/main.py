from bar_tab import Tab

table1 = Tab()

while True:
    item = input("Add item: ")
    table1.add(item)

    more = input("Add more item (y/n): ")
    if more == 'Y' or more == 'y':
        continue
    else:
        break

table1.print_bill()
