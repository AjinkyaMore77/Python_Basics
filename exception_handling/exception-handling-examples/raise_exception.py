from logging import raiseExceptions


def raise_excep():
    age= int(input('enter age'))
    if age>18:
        print('valid')
    else:
        raise Exception('age should greater than 18')
    print('rest code')
raise_excep()