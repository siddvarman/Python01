import math
#take length of the tromboloid from user
l = float(input("Enter length of the tromboloid"))
#take breadth of the tromoloid from the user
b = float(input("Enter breadth of the tromboloid"))
#take height of the tromboloid from the user
h = float(input("Enter height of the tromboloid"))
#calculate the characteristic dimension
k = (l**2) + (b**2) + (h**2)
print(k)
#calculate the volume of the tromboloid
v = (h**2) * (b**2)/k**(1/2)
print('volume of tromboloid = ',format(v,'0.3f'))
#challenge
radius = ((3*v)/(4*math.pi))**(1/3)
print('radius of tromboloid = ',format(radius,'0.3f'))
