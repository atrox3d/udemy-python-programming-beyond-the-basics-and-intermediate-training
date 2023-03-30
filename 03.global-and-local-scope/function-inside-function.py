def func():
    i = 90

    def inner():
        print(i)

    inner()


func()

# print(i) # NameError
# inner() # NameError

