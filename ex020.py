import random

a = str(input('First student:'))
b = str(input('Second student'))
c = str(input('Third student'))
d = str(input('Forh student'))

list =[a, b, c, d]
random.shuffle(list)
print(list)