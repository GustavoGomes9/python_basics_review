def phrase(lastname, /, firstname='Caco', *, age="35"): #Position-only, position-or-keyword and  argument
    print(firstname, lastname, age)

phrase('gomes','Gustavo', age='21')

def args_kwargs(text, *args, **kwargs):
    print(text)
    if args:
        print(args, '*args')
    if kwargs:
        print(kwargs, '*kwargs')

x = args_kwargs
x('gustavo', 1, 2, 3, gender="man")