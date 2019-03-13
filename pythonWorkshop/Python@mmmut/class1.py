class student(object):
    def hello(self):
        print ("heello")
    def __init__(self,a,b):
        self.c =a
        self.d  =b
    def hi(self):
        d =  self.c + self.d
        print (d)

obj =  student(30,40)
obj.hi()

