x=input ("Enter first value: ")
y=input ("Enter second value: ")

#COMPARISON OPERATORS
print (x>y)
print (x>=y)
print (x<y)
print (x<=y)
print (x==y)
print (x!=y)

#LOGICAL OPERATORS
print ((x>y) or (x==y))
print ((x>y) and (x==y))
print ( not x==y)

#MEMBERSHIP OPERATORS
print ("hell" in ("Hello")) # h and H are different as python is case sensitive
print ("hell" not in ("Hello"))
print ("Hell" in ("Hello"))
print ("Hell" not in ("Hello"))
