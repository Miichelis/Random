#Fibonacci

def fibonacci(n):
    a=0
    b=1
    print a;print b

    for i in range(2,n):
        s=a+b
        a=b
        b=s
        if i == n-1:
            return s
        else:
            print s

