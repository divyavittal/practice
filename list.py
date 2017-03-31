print"to implement fibonacci series"

a = int(input("enter starting number here:"))
b = int(input("enter ending number here:"))

def fibonacci(n):
    if (n < 2):
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
print map(fibonacci, range(a ,b))



