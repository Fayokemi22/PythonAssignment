# initialize p
# initialize r
# with the formula p = 1000 a = p(1 + r)**n
#find the nth time of 10,20 and 30


p = 1000

r =  0.07


TenYears = p * ( 1 + r) ** 10
TwentyYears = p * ( 1 + r) ** 20
ThirtyYears = p * ( 1 + r) ** 30

print("The amount on deposit at the end of the nth year is ","$", round(TenYears))
print("The amount on deposit at the end of the 20th year is ","$", round(TwentyYears))
print("The amount on deposit at the end of the 30th year is ","$", round(ThirtyYears))
