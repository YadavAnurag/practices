import sys
def hello(a,b):
    c =  int(a) + int(b)
    return c

def hi():
    return "ok"

if __name__ == "__main__":
    d = hello(sys.argv[1],sys.argv[2])
    print (d)
#d  =hello(3,4)
#print (d)
