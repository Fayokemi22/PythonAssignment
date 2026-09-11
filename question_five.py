integer=int(input("Enter number "))

sum=0
while integer>0:

    digit=integer%10
    sum+=digit
    integer//= 10

print(sum)

