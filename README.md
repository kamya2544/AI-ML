# AI-ML

Introduction to Machine Learning:
-The idea of learning from examples and experience w/o being explicitly programmed.
-Instead of writing code, we feed data to a generic algorithm, and it builds logic based on the data given.

Three types of ML:
-Supervised Learning (i/p and o/p data available)
-Unsupervised Learning (only i/p data available)
-Reinforcement Learning (expose the model to the real system and it will learn itself based on renewal or penalty)

Supervised learning:
-Dependent variable (y) and independent variable (x)
-Learns from previous data
-Two Subtypes:
	-Classification: o/p is a group or category eg-black or white, spam or not spam
	-Regression: o/p is a real value eg- rupees, height

Unsupervised Learning:
-Only i/p data is available
-System finds patterns directly from examples
-Two Subtypes:
	-Association: discover rules that describe large positions of data eg- people who buy apples tend to buy mango, on Amazon there is a "people also bought" and "often bought together" column 
	-Clustering: discover inherent clusters in data eg- kids usually purchase chocolates, boys usually purchase batteries, girls usually purchase stationery

Reinforcement Learning:
-Comp prog interacts with a dynamic environment in which it must perform a particular goal
-Depending on the task we change, the reward and penalty are decided

Applications:
-Face Detection
-Email Filtering
-Medical Diagnosis
-Weather Prediction







Python Notes

print Keyword Basic Rules:
-if we put (") or (') it gives the same output without any error since in python character and string are considered as string only
-at the end of a statement, a semicolon (;) isn't necessary

- print ("Hello!" * 3) gives output Hello!Hello!Hello!

- print ("Hello! \n" * 3) gives output  Hello!
					Hello!
					Hello!
- print ("Hello!" * 3.5) gives an error as a string can be multiplied by only an integer
- print("hi")
  print("hello")
  print("bye")
	It gives an o/p: hi
			 hello
		 	 bye
- print("hi", end='\t')
  print("hello", end='\t')
  print("bye", end='\t')
	It gives an o/p: hi	hello	bye

- print("hi", "hello", "bye")
	It gives an o/p: hi hello bye
	Here space is there after every string because there is an argument called separator whose default value is a space
	print("hi", "hello", "bye", sep=' ')

- print("hi" + "hello" + "bye")
	It gives an o/p: hihellobye
	CONCATENATION 
	No space is added by default, we can use \t or \n

-f means format string: Concept of static data used here (within curly braces{})
CASE 1
print(f"hello {2 + 2}") 
o/p is 4

CASE 2
print(f"hello {2 + 2.4}") 
o/p is 4.4

CASE 3
print(f"hello {'2 + 2'}") 
o/p is 2 + 2

CASE 4
print("hello {2 + 2.4}")
o/p hello {2 + 2.4}

CASE 5
print("hello {2 + 2.4}, format[2]")

CASE 6
print("hello {}".format(2)) prints hello 2
print("hello { }".format(2)) prints error
print("hello ".format(2)) ;prints error

COMMENTS:
"#" sign can be used to give comments within the code

ARITHMETIC OPERATORS:
+ Addition
- Subtraction
* Multiplication
/ Division
// Floor Division (gives float o/p if one or both i/ps are float)
** Exponentiation/ Power

TYPE KEYWORD:
print (type(4)) 
o/p <class 'int'>
-used to tell the type of given data
- since python is based on oops so everything is related to objects in classes

DECLARING VARIABLES:
-In Python, we don't need to specify the data type just simply write-----> a=5
- a,b,c=2,3.4,"hello" is one way of declaring in a single line
- a=2; b=3.4; c="hello" is other way

SWAPPING VARIABLES:
a,b=b,a

input KEYWORD:
-Getting input from the user
-user_inp=input ("Enter some value: ")
 print (user_inp)
-i/p can be any data type
- print (type(user_inp))
	It returns <class 'str'> because the input keyword accepts everything as string data type

ADDITION OF TWO VARIABLES:
x=input ("Enter first value: ")
y=input ("Enter second value: ")
z= (x+y) 
	It will concatenate as a string as input accepts every value as a string

print (type(z))
	o/p is <class 'str'>

a=int (input ("Enter first value: "))
b=int (input ("Enter second value: "))
c= (a+b) 
print (c)
	It will do addition since we declared int data type to input keyword

print (type(c))
	o/p is <class 'int'>

COMPARISON OPERATORS:
> < >= <= == =!
Gives o/p as true or false

LOGICAL OPERATORS:
or, and, not
Gives o/p as true or false

MEMBERSHIP OPERATORS:
in, not in
Kind of searching operator
Case sensitivity is taken into consideration 
h and H are treated differently

CONDITIONAL STATEMENTS:
- ':' isn't used for termination as in {} are used in C++ or Java but as indentation for the command statement of the condition
- if...else
- if...elif...else
- We can use as many elif statements as we want
- Checks one statement at a time and executes the statement which is true
- Can be nested as many no. of times as we want

SLICING:
- Extracting a part of data using the concept of INDEXING
- positive index (0 onwards) from left side
- negative index (-1 onwards) from right side
- spaces, tabs, punctuators etc. also have index since they occupy memory
-print (message[3])
	o/p will be the character at 3 index that is fourth character since indexing starts at 0
-print (message[0:3]) 
	o/p will be index 012
	0 index character to the character before 3 index
- [:3] from start to 3 index
- [3:] from 3 index to last
- [:] from start to end
- [0:11:2] 2 STEP INDEX --> skips one letter and prints from 0 to 11 index that is prints 0,2,4,6,8,10th index character
- [0:11:1] 1 STEP INDEX --> prints from 0 to 11 index skipping 0 characters 
- [::3] skip two values
- [::-1] REVERSING THE DATA
