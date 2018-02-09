frase = str(input('Type a franse')).upper()

print('The letter a appear {} times on this frase'.format(frase.count('A')))
print('The first letter A appear on position {}'.format(frase.find('A')+1))
print('The last letter A appear on position{}'.format(frase.rfind('A')+1))