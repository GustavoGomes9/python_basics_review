#tuples , are immutable
tuple1 = '12345', '56987', 'hello'
tuple2 = tuple1, (1,2,3,4,5)
print(tuple2) 

#set, removes redudancy
fruits = {'banana', 'dragonfruit', 'dragonfruit', 'apple'}
print(fruits)

#dictionary list of keys with arguments
dic = { #or create with dict([]) constructor
    'name': 'Gustavo',
    'age': 22,
    'email': 'gustavo@gmail.com'
}
print(dic)

# LOOP SENTENCES

# items()
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for n, i in knights.items():
     print(n, i) 

# enumerate()
for n, i in enumerate(['tic', 'toc']):
    print(n, i)

# zip()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print('What is your {0}?  It is {1}.'.format(q, a))