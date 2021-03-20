array = ['jerry', 'beth', 'rick', 'summer', 'morty']
print(array)
array.append('morty')
print(array)

array1 = ['Homer', 'Lisa', 'Bart']
array.extend(array1)
print('Extended crossover: ',array)

array.insert(6,'Marge')
print('Extended family: ',array)

array.remove('jerry')
print("We don't need him: ",array)

array.pop(2) # if .pop(), it will delete the last  data
print('No one gonna miss her: ',array)

index = array.index('morty')
print('Position',index)

count = array.count('morty')
print('How many ?',count )

array.sort() # .reverse # try it too
print('Ramdomized ',array)

data = array.copy() # ccopy a version of list
print('copied', data)

del array[2:6]
print(array)

array.clear()
print('Array',array)



 