i = 70  # global


def func():
    global i    # makes i global inside the function
    global g    # makes g global from inside the function
    i = 80      # changes the value of the global i
    g = 100     # creates a global g variable = 100
    l = 90      # local
    print(f'func | {i=}, {l=}, {g=}')


func()
print(f'{i=}')
print(f'{g=}')    # g can be addressed only after func() is executed
# print(l) # NameError
