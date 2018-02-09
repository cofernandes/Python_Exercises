salary = float(input('Please type your salary:'))

a = (10 / 100) * salary + salary
b = (15 / 100) * salary + salary

if salary <= 1250:
    print('You have a salary increase of 15% new salary is £ {} '.format(b))
else:
    print('You have a salary increase of 10% your new salary is £ {}'.format(a))

