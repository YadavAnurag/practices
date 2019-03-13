fin = open("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\input.txt","r")
fout = open("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\out.txt","w")
import re
while 1:
    str1 =  fin.readline()
    if str1:
        print (str1)
        b =  re.search("\d{10}",str1)
        if b:
            fout.write(b.group())
            fout.write("\n")
    else:
        break
fin.close()
fout.close()
 
