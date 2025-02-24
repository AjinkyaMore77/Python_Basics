def divby_zero(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('cant devide by zero')
    except TypeError:
        print('please enter integer')
    finally:
        print('rest code')
    print('ajinkya')
divby_zero(20,'10')