#!/usr/bin/python

# basic concept of classes 
'''
# basic concept of classes using calculator #####youtube sentdex 

class calculator:

	def add(self,x,y):
		print x+y	

	def mul(self,x,y):
		print x*y
			
	
	def sub(self,x,y):
		print x-y
			
	
	def div(self,x,y):
		print x/y
			

c = calculator()

c.add(2,10)
c.mul(10,2)
c.sub(10,5)
c.div(10,2)
'''

try :
	class calculator:

		def add(self,x,y):
			print x+y
			
	

		def mul(self,x,y):
			print x*y
			
	
		def sub(self,x,y):
			print x-y
			
	
		def div(self,x,y):
			print x/y
			

	c = calculator()

	Input = int (raw_input("enter the choice:"))
	
	x = int (raw_input("enter x:"))
	y = int (raw_input("enter y:"))
	
	if Input == 1:
		c.add(x,y) 
	
	elif Input == 2:
		c.mul(x,y) 

	elif Input == 3:
		c.sub(x,y) 

	elif Input == 4:
		c.div(x,y)

 	elif Input <= 5:
		print "it is not avaliable"
		exit()


except ValueError:
	"value is wrong"

