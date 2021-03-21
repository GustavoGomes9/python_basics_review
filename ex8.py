
hero = ['Batman', 'Superman', 'Aquaman']
aka = ['Bruce', 'Clark', 'Arthur']

for i, v in zip(hero, aka):
    print('{0:5} is: {1}'.format(i, v)) #you choose your format of output

# Handling Exceptions
try:
    x = 1 + 1 #try put '' to test
except:
    x = 5 + 5
else: 
    print('--------else----------')
finally:
    print(f'The number is: {x}')

# Raising exceptions
try: 
    raise NameError('test')
except NameError:
    print('Exception flew by')
    raise
 
# Exception Chaining - cadeia de exceções

def foo():
    raise IOError
try:
    foo()
except IOError as exc:
    raise RuntimeError('Failed to open database') from exc

