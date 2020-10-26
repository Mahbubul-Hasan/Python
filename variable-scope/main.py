name = 'Ryu'
# ----------------------------------
# def print_name():
#     print(f'The name inside the function is {name}')
# ----------------------------------

# ----------------------------------
def print_name():
    global name
    name = 'Yoshi'
    print(f'The name inside the function is {name}')
# ----------------------------------
print_name()
print(f'The name inside the function is {name}')
