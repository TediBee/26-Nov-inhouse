import os
#this test
price = 0

print('Welcome to Pizza Maker')
print('Hallo')
size = input('What size pizza do you want? S, M, or L?\n').lower()

if size == 's':
  price+=3
elif size == 'm':
  price+=4
elif size == 'l':
  price+=5

q = input('Do you want to add mozarella? (y/n)\n').lower()
if q == 'y':
  price+=3

q = input('Do you want to add parmesan? (y/n)\n').lower()
if q == 'y':
  price+=2

q = input('Do you want to add sausage? (y/n)\n').lower()
if q == 'y':
  price+=2

q = input('Do you want to add pepperoni? (y/n)\n').lower()
if q == 'y':
  price+=2

q = input('Do you want to add chicken chunk? (y/n)\n').lower()
if q == 'y':
  price+=2

q = input('Do you want to add paprika? (y/n)\n').lower()
if q == 'y':
  price+=2

q = input('Do you want to add tuna? (y/n)\n').lower()
if q == 'y':
  price+=3

q = input('Do you want to add shrimp? (y/n)\n').lower()
if q == 'y':
  price+=3

q = input('Do you want to add pineapple? (y/n)\n').lower()
if q == 'y':
  price+=2

os.system('clear')
print(f'Thank you for your order. Your pizza price is ${price}')