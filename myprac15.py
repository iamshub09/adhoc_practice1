#!/usr/bin/python

# statistics pakage modules mean avg standard deviations etc and perfom only in python 3 

'''
statistics is a module we have to install these module for importing in any program .
so pip command is used to install modules

# install pip 

###### pi
###### yum repolist all
###### yum install python-pip

# install modules by using pip
 
######   pip install module_name_
######   pip install scipy
######   pip install statistics

 and, before install module we have to install pip also which is used to install modules

'''

import statistics

example_list1=[4,6,2,6,7,8,2,5,7,6,8,4,6,7,2,2]
x= statistics.mean(example_list1)
print x


 
example_list2=[4,6,2,6,7,8,2,5,7,6,8,4,6,7,2,2]
y= statistics.median(example_list2)
print y

example_list3=[4,6,2,6,7,8,2,5,7,6,8,4,6,7,2,2]
z= statistics.stdev(example_list3)
print z

example_list4=[4,6,2,6,7,8,2,5,7,6,8,4,6,7,2,2]
h= statistics.variance(example_list4)
print h

