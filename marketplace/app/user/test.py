

def teile2(zahl):
    try:
        return 5 / zahl
    except ZeroDivisionError as error:
       print(error)

    


teile2(0)

