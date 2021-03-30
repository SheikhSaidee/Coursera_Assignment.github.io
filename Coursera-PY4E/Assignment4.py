def computepay(h,r):
    if h<=40 :
    	pay=h*r
    else :
        hr=h-40
        temp=hr*1.5*r
        pay=(h-hr)*r
        pay=temp+pay
    return pay

hrs = input("Enter Hours:")
rate= input("Enter the rate per hour: ")
h =float(hrs)
r =float(rate) 
p = computepay(h,r)
print("Pay",p)
