#!/usr/bin/python

# writing to a file

text = 'KARAN \n ARJUN '
text1 = 'SONU\n a KAKU '


saveFile = open('/root/Desktop/python/exampleFil1.txt','w') 
saveFile2 = open('/root/Desktop/python/exampleFil2.txt','w')

saveFile.write("hello shubham mathur")
saveFile2.write(text1)

saveFile.close
saveFile2.close


# appending to a file

appendMe= '\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n hello friends chai peelo'

appendFile=open('/root/Desktop/python/exampleFil1.txt','a')
appendFile.write(appendMe)
appendFile.close()

# read from a file 

#readMe=open('/root/Desktop/python/exampleFil1.txt','r').read()
readMe=open('/root/Desktop/python/exampleFil1.txt','r').readlines()

print readMe




