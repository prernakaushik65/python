#Calculate the Hyptonuse of right angled triangle and input base and height from useer!
import math
print("Calculate Hypotonuse here")
b = int(input("Enter the value of base"))

p = int (input("Enter the value of height"))

#h = math.sqrt(b*b + p*p)
h = math.sqrt(pow(b,2)+pow(p,2))

print("Hypotonuse = ",h)
