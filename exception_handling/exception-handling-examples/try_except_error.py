def divby_zero(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('cant devide by zero')
    except TypeError:
        print('please enter integer')
divby_zero(0,10)

