price = float(input('What is the price of the product'))

x = price * 5
y = x /100
descont = price - y

print('The new price of this product is {}'.format(descont))