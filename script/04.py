#################################################################
#################### PROBLEM 04 #################################
#################################################################

"""

Write a program to convert the time inputted in minutes into hours and remaning minutes.

"""

## SOLUTION

time = int(input("Enter the time in minutes:"))

hours = time/60
mins = time%60

print("Hours are:", hours)
print("Minutes are:", mins)


