class A(object):
    def hello(self):
        print ("aaaa")
class B(A):
    pass
class C(A):
    def hello(self):
        print ("ccccc")
class D(B,C):
    pass
print (D.__mro__)
obj = D()
obj.hello()

               
