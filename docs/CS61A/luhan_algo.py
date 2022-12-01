digit = lambda x: 2*x if 2*x<10 else (2*x//10)+((2*x)%10))
def s(n):
    ##ITERATIVE
    k = 0
    sumthing = 0
    while n>0:
        if k%2==1:
            sumthing += digit((n%10)*2)
        else:
            sumthing += n%10
        n=n//10
        k+=1
    print(sumthing)
    return sumthing
