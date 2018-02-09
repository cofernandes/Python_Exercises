house =  float(input('how much the house cost £: '))
salary = float(input('How much money do you earn per month £: '))
pay = int(input('How long do you wanna pay your loan? '))

month = house / (pay * 12)
loan = salary * 30 / 100

if month <= loan:
    print('Your loan has been approved will pay per month {:.2f}'.format(month))
else:
    print('Sorry but your loan has been denied because {:.2f} is bigger then {:.2f}'.format(month, loan))

