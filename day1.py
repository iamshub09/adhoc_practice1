#!/usr/bin/python

import time 

# for print

print "hello"
time.sleep(2)
print "       "

# variable creation

x=100
y=200
z=x+y
print z
time.sleep(2)
print "       "

# swaping

c=10
d=20
c,d=d,c
print "value of c is :" 
print c

print "value of d is :" 
print d
time.sleep(2)
print "       "

# immutable datatype variable addressing 
#same address pe valie change nahi ho skti

a=10
print id(a)
print id(10)
print "       "

b=20
print id(b)
print id(20)
print "       "

e=10
print id(e)
print id(10)
time.sleep(2)
print "       "

# immutable datatypes (int, float, string )

m=500
print type(m)
print "       "

n=50.50
print type(n)
print "       "

f="this is string"
print type(f)
time.sleep(2)
print "       "

#string operations 

print f+' '+"word spacing and concat"
time.sleep(2)
print "       "

g=f+' '+"word spacing and (concat) and (save string in a variable)"
print g
time.sleep(2)
print "       "

print "length of a string is "
print len(g)
time.sleep(2)
print "       "

k="HEY"
print k*10
print "       "

# print k+10

print x*10
print x+10
time.sleep(2)
print "       "

#upper and lower case
print "upper to lower and lower to upper case "
l="captial and SMALL"
print l.upper()
print "       "
p=l.lower()
print p

#how variable shown in graphs 

v="hello"
print v
#positive

print v[0]
print v[1]
print v[2]
print v[3]
print v[4]
print " "

time.sleep(2)

#negative

print v[0]
print v[-1]
print v[-2]
print v[-3]
print v[-4]

print " "

time.sleep(2)

#the last ratio digit is not shown example in 0:4 4 is not showing  

print v[0:4]

print v[0:3] in v
 
