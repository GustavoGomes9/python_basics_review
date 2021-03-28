# odds and ends
class Something:
    """ Nothing here """
    pass

s = Something()
s.name = 'Gustavo'

#print(s.__doc__)
#print(s.name)
#dir(s)

for line in open("ex13.txt"):
    print(line, end='')
