'''
x=input ("Enter first value: ")
y=input ("Enter second value: ")

#CONDITIONAL STATEMENTS
if x>y:
    print (x, 'is greater')
elif x<y:
    print (y, 'is greater')
else:
    print ('Both are equal')
    
'''
#NESTED CONDITIONAL STATEMENTS
user, pswd= 'user', 'pswd'
username= input('Enter the username')

if username==user:
    password= input ('Enter the password')
    if password==pswd:
        print ('Login Successful')
    else:
        print ("Wrong password")
else:    
    print ("User does not exist")
