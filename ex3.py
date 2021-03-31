def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
a = ask_ok
a("")

def f(a, L=[]):
    L.append(a) #it adds a new element at the end of the list
    return L

print(f(1))
print(f(2))
print(f(3))