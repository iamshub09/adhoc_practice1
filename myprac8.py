#!/usr/bin/python

import time 
# how to create functions 

# def keyword used to create a function 

def example():
	print"this is my function example"
	x=5+9
	print x


example()


# function parameters
print "  "
time.sleep(2)


def addtion(num1,num2):
	ans=num1+num2
	print "num1 is ",num1  # add string with integer using comma
	print "num2 is ",num2
	print ans

#addtion(2,3)
#addtion(2) one variable showing error
#addtion(2,3,4) variable showing error coz (((parameter variable ==  passing variable value))) 
addtion(num2=2,num1=3) # order changed in order to parameter and give the value explictly



# function defaults
print "  "
time.sleep(2)

# we can define that fuction later using pass
def fundef1(num1,num2):
	pass

def fundef1(num1,num2=10):
	ad=num1*num2
	print ad 

fundef1(10)

def basic_window(width,height,font='TNR',
		 bgc='w',scrollbar=True): #managed in a proper way

	print width,height,font,bgc

basic_window(10,20,'a',bgc='Red') #font and bgc can be affected cz i changed in a value 



