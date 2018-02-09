number = int(input('Please type a number to be convert'))
choice = int(input('what is your choice to be convert 1 binary, 2 octal or 3 hexadecimal'))

if choice ==1:
    print('Binary: {}'.format(bin(number)[2:]))
elif choice ==2:
    print('Octal {}'.format(oct(number)[2:]))
elif choice ==3:
    print('Hexadecimal{}'.format(hex(number)[2:]))

