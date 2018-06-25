#!/usr/bin/python

import time

#global and local variables

'''
global variable can access anywhere

local variable can access in environemnet orits frame it can not access globally in a program
'''
# 1
time.sleep(3)
print " "

x=6
def example():
	z=5
	print z	
	print x
	print x+5 # we can play with variable
'''	
	#x+=6
	#print x

shown error we can not change the value of x we just assign or play with local variable for changing the value of local variable we need to use global variable. 	
'''


example()

# 2
time.sleep(3)
print " "

y=10
def example2():
	global y
	print y	
	y+=6  # use of global we can change the value
	print y

example2()

# 3
time.sleep(3)
print " "


g=30
def example3():
	globg = g
	print globg	
	globg+=20
	print globg

example3()

# 4
time.sleep(3)
print " "

r=30
def example4():
	globr = r
	print globr	
	globr+=20
	#print globr
	return globr
r = example4()
print r
