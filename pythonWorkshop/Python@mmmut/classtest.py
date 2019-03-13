class student(object):
    def __init__(self,val1,val2):
        self.c = val1
        self.d = val2
    def summe(self):
        f = self.c +  self.d
        print (f)
obj = student(34,43)
obj.summe()
