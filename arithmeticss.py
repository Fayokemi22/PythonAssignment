# Collect the input from users
# do the sum of the inputl collected
# do the average of the inputl collected
# do the product of the inputl collected
# find the smallest number
# find the largest number


first_number = int(input("The first number is"))

second_number = int(input("The second number is"))

third_number = int(input("The third number is"))

sum = first_number + second_number + third_number

average = (first_number + second_number + third_number
) / 3

product = first_number * second_number * third_number

smallest = min(first_number, second_number,third_number)

largest = max(first_number,second_number,third_number)

print("The sum is", sum)

print("The average is", round(average,2))

print("The product is", product)

print("The smallest is", smallest)

print("The largest is", largest)

