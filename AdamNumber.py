'''
12 is the no
square is 144
reverse of square is 441
root is 21
reverse is 12
initial and final no is 12 so it is adam no
'''
inp=int(input('Enter a number: '))
out=int(str(int(int(str(inp**2)[::-1])**0.5))[::-1])
if inp==out:
    print (inp, 'is a adam number')
else:
    print (inp, 'is not an adam number')
