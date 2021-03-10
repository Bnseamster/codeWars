def litres(time):

    if type(time) != int and type(time) != float:
        raise Exception(f'Invalid input received, input of type {type(time)} should be type {int} or {float}')
    if time < 0:
        raise Exception('Input time cannot be negative')
    return int(time*.5)

