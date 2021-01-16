#################################################################
#################### PROBLEM 03 #################################
#################################################################

"""
Write a Python code to calculate simple interest by inputting the value of Principal amount and rate from the user for a time period of 5 years.

"""

## SOLUTION

Principal = eval(input("Enter the value of Principal:"))
Rate = eval(input("Enter the annual rate of interest:"))
Time = 5

Simple_int = Principal*Rate*Time / 100   # SI = P*R*T/100
Amount = Principal + Simple_int          #  A = P + SI

print("Simple Interest = ₹", Simple_int)
print("Amount payable = ₹", Amount)


