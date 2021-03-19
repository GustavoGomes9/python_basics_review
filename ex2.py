for w in range(20):
    print(w)
    #print(sum(range(20)))

endloop = int(input("put the end of the loop ?"))
for i in range(endloop):
    if i >= 20:
        print("20 is here")
        break
else:
    print(i)

core = ['Henry cavil', 'Ben affleck', 'Gal gadot']
for i in range(len(core)):
    print(i, core[i])