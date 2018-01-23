i=0
print "While loop example"
while (i<3):
    print i,
    i+=1
print ""

print "List example"
l= [1,2,3,4]
for j in l:
    print j,
print ""

print "Tuple example"
t = {1,2,3,4}
for k in t:
    print k,
print ""

print "Dictionary example"
d = {"A":1, "B":2}
for a in d:
    print "%s %d" %(a,d[a])

print "Dicc Iterator"
d = {"A":1, "B":2, "C":3}
for key,value in d.iteritems():
    print (key,value),


