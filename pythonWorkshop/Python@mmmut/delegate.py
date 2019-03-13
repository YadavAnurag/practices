class mylist(object):
    def __init__(self,a):
        self.alist = a
    def append(self,elem):
        self.alist.append(elem.upper())
    def pop(self,index):
        print ("u cannot pop")
    def __getattr__(self,method):
        print (method)
        return getattr(self.alist,method)

b = [1,2,3,65,43,12,56]
obj = mylist(b)


obj.pop(1)
print (b)
'''
obj.sort()
print (b)
obj.reverse()
print (b)
obj.insert(0,45)
print (b)
'''
