import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'My math script')

    # -----------------
    # parser.add_argument('number1', help = 'Number 1', type=float)
    # parser.add_argument('number2', help = 'Number 2', type=float)
    # parser.add_argument('operator', help = 'Provide operator')
    # -----------------

    # -----------------
    # parser.add_argument('--number1', help='Number 1', type=float)
    # parser.add_argument('--number2', help='Number 2', type=float)
    # parser.add_argument('--operator', help='Provide operator', default = '+')
    # -----------------

    # -----------------
    parser.add_argument('-n1', '--number1', help='Number 1', type=float)
    parser.add_argument('-n2', '--number2', help='Number 2', type=float)
    parser.add_argument('-o', '--operator', help='Provide operator', default = '+')
    # -----------------

    args = parser.parse_args()
    print(args)
    result = None
    if args.operator == '+':
        result = args.number1 + args.number2
    
    if args.operator == '-':
        result = args.number1 - args.number2
    
    if args.operator == '*':
        result = args.number1 * args.number2
    
    if args.operator == '/':
        result = args.number1 / args.number2
    
    print(result)
