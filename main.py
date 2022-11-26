import os

def register():
  while True:
    username = input('Username : ')
    if os.path.exists(f'{username}.txt'):
      print('Username already exists.')
      continue
    break
  password = input('Password : ')
  full_name = input('Your full name : ')
  while True:
    gender = input('Your gender (M/F) :  ').lower()
    if gender != 'm' and gender != 'f':
      print('Please input M/F only.')
      continue
    break
  while True:
    try:
      age = int(input('Your age (number) : '))
      break
    except:
      print('Please input number only.')
  
  f = open(f'{username}.txt','w')
  f.write(f'''{password}
{full_name}
{gender}
{str(age)}''')
  f.close()
  input('Your account has been registered successfully.\nPress enter..')

def login():
  username = input('Username : ')
  password = input('Password : ')
  if os.path.exists(f'{username}.txt'):
    f = open(f'{username}.txt','r')
    p = f.readline().strip('\n')
    fn = f.readline().strip('\n')
    g = f.readline().strip('\n')
    a = f.readline()
    f.close()
    if password == p:
      print(f'''
Welcome, {fn}
this is your info:
Gender : {g.upper()}
Age : {a}''')
    else:
      print('Incorrect password.')
  else:
    print('User not exists.')
  input('Press enter to continue..')

while True:
  os.system('clear')
  print('Welcome to CBA-Link')
  print('''1. Login
2. Register
3. Quit''')
  c = input('Choice (1-3) : ')
  os.system('clear')
  if c == '1':
    login()
  elif c == '2':
    register()
  else:
    quit()