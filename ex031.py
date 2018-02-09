km = int(input('how many Kms is your journey:'))
m1 = km * 0.50
m2 = km * 0.45

if km <= 200:
    print('You have to pay on this toll £{}'.format(m1))
else:
    print('You have to pay on this toll an amount of £{}'.format(m2))
