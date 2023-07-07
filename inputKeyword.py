#GETTING I/P FROM THE USER:
user_inp=input ("Enter some value: ") #input keyword always accepts every value as a string data type 
print (user_inp)
print (type(user_inp)) # It gives o/p <class 'str'> always

#ADDITION OF TWO VARIABLES:
x=input ("Enter first value: ")
y=input ("Enter second value: ")
print (x+y) #it will concatenate as a string
a=int (input ("Enter first value: "))
b=int (input ("Enter second value: "))
c= (a+b) #it will do addition since we declared int data type to input keyword
print (type(c)) #type casting is done
