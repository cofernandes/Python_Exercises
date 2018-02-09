a = float(input('Please type the first line'))
b = float(input('Please type the second line'))
c = float(input('Please type the third line'))

if a < b + c and b < a + c and c < b + a:
    print('\033[1;31mWith these lines we have a triangle')
else:
    print('\033[1;35m not a triangle')


