# Take money borrowed, interest and duration as input. Then, compute the compound interest rate.

# compound interest formula is:
# a = p*(1 + (r/100))*t


# Here, P is the principal amount; 
# it is the amount that you borrowed. 
# r is the interest rate in percentage and t is the time

p = float(input('Enter the amount of money principle: '))
r = float(input('Enter the rate of interest: '))
t = float(input('Enter the time for how long you borrowed: '))

a = p*(1 + (r/100))*t

print('the amount of total interest after 5 years', round(a))

