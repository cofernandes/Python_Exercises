import random

a = input('Fist student:')
b = input('Second student')
c = input('third student')
d = input('Fourth student')

lista = [a, b, c, d]

r = random.choice(lista)
print(r)