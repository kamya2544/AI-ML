#SLICING
message="How are you all?"
print (len(message)) #prints the length of message

#WAY 1    
print (message[0])
print (message[3]) #prints space since space also has index 
print (message[-1])
print (message[4])

#WAY 2
print (message[len(message)-1]) #since indexing starts at 0 so last character is length-1 not the length
print (message[(int((len(message)-1)/2))]) #print middle character

#WAY 3
print (message[(len(message)-1)//2]) # floor division doesn't always work

#TO PRINT SPECIFIED LETTERS
print (message[0:3])
print (message[:3])
print (message[3:])
print (message[:])
print (message[0:11:2])
print (message[::3])

#DATA REVERSING
print (message[::-1])
