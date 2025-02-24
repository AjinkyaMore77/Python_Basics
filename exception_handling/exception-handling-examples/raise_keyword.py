def except1():

    age= int(input("enter age"))
    try:
        if age>18:
            print('age is valid')
        else:
            raise Exception("not process")
    except Exception as ajinkkya:
        print(ajinkkya)
except1()