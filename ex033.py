n1 = int(input('Type a number'))
n2 = int(input('Type a more number'))
n3 = int(input('Type other number'))

if n1>n2 and n1>n3:
    biggest = n1
if n2>n1 and n2>n3:
     biggest = n2
if n3>n1 and n3>n2:
     biggest = n3

if n1<n2 and n1<n3:
    smaller = n1
if n2<n1 and n2<n3:
    smaller = n2
if n3<n1 and n3<n2:
    smaller = n3

print('The biggest number is {}'.format(biggest))
print('The smaller number is {}'.format(smaller))
