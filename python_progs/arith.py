def add(n1,n2):
    return(n1+n2)

def sub(n1,n2):
    return(n1-n2)

def mul(n1,n2):
    return(n1*n2)

def div(n1,n2):
    return(n1/n2)
def root(n1):
    return(n1*n1)

a=int(input("Enter a num1:"))
b=int(input("Enter a num2:"))
print("sum=",add(a,b))
print("sub=",sub(a,b))
print("mul=",mul(a,b))
print("div=",div(a,b))
n=int(input("Enter a num1:"))
print(root(n))
