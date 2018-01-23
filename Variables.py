# Python programs are not compiled, rather they are interpreted.
import operator

a=3
b=9

if b%a==0 :
    print "b is divisible by a"
    print "Initial value of b was 9"
else :
    print "Done with execution"


def checkdivisibility (a,b):

    if a%b==0:
        print "a is divisible by b"
    else:
        print "a is not divisible by b"

checkdivisibility(9,3)

# Global and local variable
# Global variables are the one that are defined and declared outside a function and we need to use them inside a function.

# Packing and unpacking concept from GFG
# * used for tuples and ** used for dictionaries
# Dictionary is like key value pair. Hashmap and hashtable
# defined as
d = {'a':2, 'b':4, 'c':10} #dictionary is defined


#  Hashing in python

def fun (**keyval):
    for key in keyval:
        print "%s=%s" % (key, keyval[key])

fun (Name= "Yash", Surname= "Agrawal")


l = [1,2,3,4,5]
print("Original List is :")
for i in range(0, len(l)):
    print l[i],
print ""

operator.setitem(l,3,8)
print("Set Item List is :")
for i in range(0, len(l)):
    print l[i],
print ""

operator.getitem(l,3)

