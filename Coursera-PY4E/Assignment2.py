hrs = input("Enter Hours:")
rate=input("Enter the rate per hour: ")
try:
    h = float(hrs)
    r =float(rate)
except:
    print("please enter the valid number")
    # quit() It should b used if the rest of variable becomes unrecognised because
    # program dosenot move to the next step as error occurs and it jumps to except
    # so that no error from the compiler is shown only the error which we want to show   
if h<=40 :
    pay=h*r
else :
    hr=h-40
    temp=hr*1.5*r
    pay=(h-hr)*r
    pay=temp+pay
print(pay)
	