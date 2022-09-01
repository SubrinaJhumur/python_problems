# Compute gravitational force between two objects.

# The formula for gravitational force is

# F = G m^1m^2/r^2

# Here G is the gravitational constant. Its value is 6.673*10-11

# So, take three input from the users. The mass of the first object, the mass of the second object and the distance between them.


# 


m1=float(input("Enter the first mass: "))
m2=float(input("Enter the second mass: "))
r=float(input("Enter the distance between the centres of the masses: "))
G=6.673*(10**-11)
f=(G*m1*m2)/(r**2)
print("Hence, the gravitational force is: ",round(f,2),"N")

