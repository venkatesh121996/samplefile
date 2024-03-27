def fibonacci(a,b):
    d=[a,b]
    for i in range(10):
        c=a+b
        a=b
        b=c
        d.append(c)
    print(d)

fibonacci(0,1)