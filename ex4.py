def phrase(lastname, /, firstname='Caco', *, age="35"): #Position-only, position-or-keyword and  argument
    print(firstname, lastname, age)

phrase('gomes','Gustavo', age='21')

def args_kwargs(text: str, *args, **kwargs):
    print(text, args_kwargs.__annotations__) #__annotations__
    if args:
        print(args, '*args')
    if kwargs:
        print(kwargs, '*kwargs')

x = args_kwargs
x('gustavo', 1, 2, 3, gender="man")

def document_func():
    """--Just comments 
-------------
    --Really nothing here """

print(document_func.__doc__) #__doc__