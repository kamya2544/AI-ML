# DECLARING MULTIPLE VARIABLES IN A SINGLE LINE
a,b,c=2,3.4,"hello" #way1

a=2; b=3.4; c="hello" ##way2

print (a)
print (b)
print (c)

# SWAPPING ELEMENTS
a,b=b,a
print (a,b)

#CONCATENATION OF DIFFERENT DATA TYPES USING TYPE CASTING
print (a+b+c) #not possible to add string with other data type
print (a+b) #possible using concept of arithmetic operators
print (str (a+b)+c) #possible
print (str(a+b+c)) #possible
print (int(b)) #TYPE CONVERSION/CASTING
print (float(a)) #TYPE CONVERSION/CASTING

