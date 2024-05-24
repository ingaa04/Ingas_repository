def fib(number):
    total = 0
    a = 0
    b = 1
    count = 0
    while count < number:
        nth = a + b
        a = b
        b = nth
        count = count + 1

    if a%2==0:
        print(a)
    else:
        print("not even")
    return a
fib(102)