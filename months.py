'''
Month name as first three alphabets
janfebmaraprmayjunjulyaugsepoctnovdec
Ask user to input a nonlocalif he inputs 7 print july
dont use conditions if else

concept
1   jan    month[0:3]
2   feb    month[3:6]
3   mar    month[6:9]
.
.
.
12  dec    month[33:36]

'''

month='janfebmaraprmayjunjulaugsepoctnovdec'
num=int(input('Enter a number from 1 to 12: '))
print (month[(num-1)*3:(num-1)*3+3])

#USING CONDITIONAL STATEMENTS
if num==1:
    print ('jan')
    print (month[0:3])
elif num==2:
    print ('feb')
    print (month[3:6])
elif num==3:
    print ('mar')
    print (month[6:9])
elif num==4:
    print ('apr')
    print (month[9:12])
elif num==5:
    print ('may')
    print (month[0:15])
elif num==6:
    print ('jun')
    print (month[15:18])
elif num==7:
    print ('jul')
    print (month[18:21])
elif num==8:
    print ('aug')
    print (month[21:24])
elif num==9:
    print ('sep')
    print (month[24:27])
elif num==10:
    print ('oct')
    print (month[27:30])
elif num==11:
    print ('nov')
    print (month[30:33])
elif num==12:
    print ('dec')
    print (month[33:36])
else:
    print ('wrong input')
   





