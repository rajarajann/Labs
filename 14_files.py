fout = open ("newfile.txt", "w")
line1 = "My name is Raj : Hello world\n"
fout.write (line1)
line2 = "This is the second line\n"
fout.write (line2)

x = 100
fout.write(str(x))
camels = 50
fout.write ("%d" %camels)
fout.write ("\nThere is %d number of camels" % camels)
#'%d' to format an integer, '%g' to format a floating-point number, and '%s' to format a string
fout.write("\n in %d years, I have seen %d number of %s" %(2,camels,"camels"))
import os
cwd = os.getcwd()
fout.write(cwd)
abspath = os.path.abspath("newfile.txt")
fout.write(abspath)
print (os.path.exists("newfile.txt"))
print (os.path.isdir("newfile.txt"))
#print (os.path.isdir("/home/aadhith/Python/github/Labs"))
print (os.path.isfile("newfile.txt"))
#print (os.listdir("/home/aadhith/"))
#print (type(os.listdir("/home/aadhith/")))

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            fout.write(path)
        else:
            walk(path)
#walk ("/home/aadhith/Python")
#Handling an exception with a try statement is called catching an exception
try:
    fin = open('bad_file')
except:
    print('Something went wrong.')

#pipes concept not clear
"""cmd = "ls -l"
fp = os.popen (cmd)
print (fp) #this is an object

res = fp.read (fp)
print (res)"""

#def linecount (filename):
"""    count = 0
    for line in open (filename):
        count += 1
    return count

print (linecount ("wc.py"))"""

import wc
print (wc.linecount("wc.py"))


