import ex12_self as docpython

user = docpython.User("Gustavo","Gustavo@gmail","Pass-word123")
print(user.find_all())
user.set_name('João')
print(user.find_all())
print(user.get_password())
