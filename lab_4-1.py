# Author: ATN 9/17/21

a = 1
b = 2
c = 3
x = 2
y = 5

# Split up equation:

# frac_1 = (3 + 4 * x) / 5

# frac_2 = (10 * (y - 5) * (a + b + c) ** 2) / x

# frac_3 = 9 * (((4) / x ** 2) + (9 + x) / y)

# answer = frac_1 - frac_2 + frac_3

answer = ((3 + 4 * x) / 5) - ((10 * (y - 5) * (a + b + c) ** 2) / x)\
     + (9 * (((4) / x ** 2) + (9 + x) / y))

print(answer)
