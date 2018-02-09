Name = str(input('Please type your full name')).strip()
n = Name.split()

print('Your first name is {}'.format(n[0]))
print('Your last name is {}'.format(n[len(n)-1]))
