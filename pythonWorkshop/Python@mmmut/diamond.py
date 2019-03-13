class A:
    x = 20
class B(A):
    pass
class C(A):
    x =  100

class D(B,C):
    pass

obj = D()
print (obj.x)
