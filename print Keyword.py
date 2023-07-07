print ("Hello!" * 3) #case1

print ("Hello! \n" * 3) #case2

print ("Hello!" * 3.5) #case3 (execution stops after this statement, so put 3 before this to test other statements)

print("hi") #case4
print("hello")
print("bye")
	
print("hi", end='\t') #case5
print("hello", end='\t')
print("bye", end='\t')

print("hi", "hello", "bye") #case6

print("hi" + "hello" + "bye") #case7

print(f"hello {2 + 2}") #format case1
print(f"hello {2 + 2.4}") 

print(f"hello {'2 + 2'}") #format case2

print("hello {}".format(3)) #format case3
