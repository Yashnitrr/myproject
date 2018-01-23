# Doubt 1: Suppose list contains different data types, then how to compare them while using max & min method of list

n= ord('A')
print(n)
list1,list2 = [1000,45,"h"],[21]
print "comparison will return"
print cmp(list1,list2)
print "Max will return"
print max(list1)
print min (list1)

list33, list34 = ['a'],['B']
print "Checking for ASCII"
print cmp(list33,list34)
print list1.count(1)
#list1.append(list2)
#print list1
list1.extend(list2)
print list1
print "Index of 45 is", list1.index(45)
list1.remove(21)
print list1

str = "abs12345"
lst = []
st=""
for i in range(0,len(str)):
    if str[i].isdigit():
       lst.append(str[i])

print lst

list = [1,2,3,4,5]
print sum(list)

