# My way
def fizz_buzz(input):
    if ((input % 3) == 0) and ((input % 5) == 0):
        return 'fizzbuzz'
    elif ((input % 3) == 0) or ((input % 5) == 0):
        if ((input % 3) == 0):
            return 'fizz'
        # else:
        return 'buzz'
    # else:
    return input


user_input = int(input('enter a number: '))
R = fizz_buzz(user_input)
print(R)


# More simpler way:
def fizzbuzz1(input):
    if input % 3 == 0 and input % 5 == 0:
        return 'fizzbuzz'
    if input % 3 == 0:
        return 'fizz'
    if input % 5 == 0:
        return 'buzz'
    return input


S = fizzbuzz1(7)
