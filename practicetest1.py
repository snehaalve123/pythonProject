class A:
    def formula(n):
        n1= int('%s'% n)
        n2=int('%s%s'%(n,n))
        n3=int('%s%s%s'%(n,n,n))
        print(n2)
        print(type(n2))
        c= n1+n2+n3
        return c
obj = A
n= input("enter no.")
print(obj.formula(n))