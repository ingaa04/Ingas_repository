def multiples(number):
    if number%3==0:
        print("Number is a multiple of 3!")
    else:
        print("Number is not a multiple of 3!")
    return number%3
multiples(15)