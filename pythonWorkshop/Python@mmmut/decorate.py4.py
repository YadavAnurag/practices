import time
def decorate(fn):
    def wrapped(*args):
        a = time.time()
        print ("before actual call")
        fn(*args)
        b = time.time()
        c = b - a
        print ("time taken for " + fn.__name__ + " = " + str(c))
    return wrapped


#### pawan(5,6) -  decorate(pawan)(5,6)
@decorate
def pawan():    
    print ("pawan")

@decorate
def hello():
    print ("hello")
    
f = pawan()
print (f)
s = hello()
print (s)
