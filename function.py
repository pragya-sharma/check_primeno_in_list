Aim: Check prime no in list
def prime(i):
    for k in range(2,i):
        if i%k==0:
            return False
        else:
            return True
a=[2,3,4,5,6,7,8,9]
print(a,type(a))
b=list(map(prime,a))
print(b)
