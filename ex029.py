print('-' * 60)
speed = int(input('What was your speed at that moment'))
print('-' * 60)
m = (speed - 80)*7

if speed > 80:
    print('You were over of speed limit, so you have to pay fee of {}'.format(m))
else:
    print('Well done!! speed limit ok')
