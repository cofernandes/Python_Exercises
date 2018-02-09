number1 = int(input('Type a number: '))
number2 = int(input('type second number: '))

if number1 > number2:
    print('The first number typed {} is begger  than {}'.format(number1, number2))
elif number1 < number2:
    print('The second number typed {} is bigger than {}'.format(number2, number1))
elif number1 == number2:
    print('There  is no bigger number both are the same')

