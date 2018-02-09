from random import randint
computer = randint(0, 5)
print('-' * 60)
print('I am gonna think in a number between 0 and 5, try to guess...')
print('-' * 60)
player = int(input('which number I thought? '))
if computer == player:
    print('Well done your are really good')
else:
    print('No you did not get it I thought {} not in {}'.format(computer, player))

