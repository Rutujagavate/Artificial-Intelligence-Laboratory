
#    NAME: GAVATE RUTUJA PANDURANG
 #   PRACTICLE NAME: INTRODUCTION TO PYTHON CODING

################################################################################

#Program to check if a number is prime or  not
#input from the user

num=int(input("Enter a number::"))
if (num>1):
    for i in range (2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            break;
else:
    print(num,"is a prime number")
    #Else if the input number is less than or equal to else:
    print(num,"is not a prime number")



'''*******************  OUTPUT  *********************
    Enter a number::9
    9 is not a prime number

'''



############################################################################################

#swapping of two numbers

x=5
y=10
# to take inputs from the user
x=input("Enter the value of x:")
y=input("Enter the value of y:")

# create a temporary variable and swap the value 

temp=x
x=y
y=temp
print("The value of x after swapping:{}".format(x))
print("The value of y after swapping:{}".format(y))



'''****************** OUTPUT ****************************
    Enter the value of x:5
    Enter the value of y:10
    The value of x after swapping:10
    The value of y after swapping:5
'''

##########################################################################################
# leap year

year=2000

if(year%400==0)&(year%100==0):
    print("{0} is a leap year".format(year))

# year is divided by 4  is a leap year
elif(year%4==0)&(year%100!=0):
    print("{0} is a leap year".format(year))

elif(year%4==0)&(year%100!=0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))


'''************************* OUTPUT *********************8
    2000 is a leap year
'''