# You borrowed $10000 for 28 years with 5% interest per year. Calculate the simple interest to know how much you have to pay?

# here principle p = $10000
# time t = 28 years
# interest rate r = 5%

# total interest I = p*r*t/100

p = float(input('Enter the money you borrowed: '))
r = float(input('Enter the interest rate of borrowed money: '))
t = float(input('Enter the time duration for you borrowed money: '))

I = (p*r*t)/100

print('the amount of total interest after 28 years', round(I) )

