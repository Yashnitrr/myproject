import collections
from collections import Counter
import os
import threading
'''
dict1 = {"aame":'Yash', 'Surname':'Agrawal'}
dict2 = {'Zame':'Gunjan', 'Surname': 'Agrawal'}
print cmp(dict1,dict2)
for i in dict1.keys():
    print dict1[i]

print os.getcwd()
'''


f1 = open("part1.txt","r")
#f1.write("First first first file writing in Python")
str1 = f1.read()
f1.close()
print "Str1 is %s" %(str1)

f2 = open ("part2.txt", "r")
#f2.write("second file writing in Python")
str2 = f2.read()
f2.close()
print "Str2 is %s" %(str2)

final_str = str1+" "+str2
print "Final String is %s" %(final_str)
#c = c.tolowercase()
sCount=0
str = ""
dict ={}
for i in range(0, len(final_str)):
    if final_str[i]==" ":
        sCount+=1
        if str=="":
            continue
        elif dict.has_key(str):
             dict[str]+=1
             str = ""
        else:
            dic1 = {str: 1}
            dict.update(dic1)
            str=""

    else:
        str += final_str[i]
if str!= "":
    if dict.has_key(str):
             dict[str]+=1
             str = ""
    else:
            dic1 = {str: 1}
            dict.update(dic1)
            str=""

dic5 = {" ":(sCount-1)}
dict.update(dic5)
print Counter(dict)
