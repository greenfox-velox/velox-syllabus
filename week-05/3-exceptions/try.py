number = 1

def ujjaj(num):
    msg = ''
    if num == 1:
        msg = 'egy'
    if num == 2:
        msg = 'ketto'
    if num < 3:
        raise ValueError(msg)
    

try:
  print('hello')
  18 / 0
  ujjaj(number)
  print('a szam frankon nagyobb mint ketto')
except ValueError as e:
  print('sajna a szam')
  print(e)
except Exception as err:
  print(type(err))
  print('Hiiinye de ne osszal nullaval ecsem')

