#******************************************MAP********************************************************
#convert string to integer in map
list_in_string = ["1", "2", "3"] 
result = list(map(int,list_in_string))
print(result)

#add 10 to each elelment in the list
def add_ten_to_each(numbers):
    return numbers + 10
    
numbers =  [0, 5, 10, 15]
result = map(add_ten_to_each,numbers)
print(list(result))

#Write a map() function to convert temperatures from Celsius to Fahrenheit
def convert_temperatures_from_Celsius_to_fahrenheit(celsius):
    return celsius * 1.8 +32
    
numbers =  [0, 20, 37, 100]
result = list(map(convert_temperatures_from_Celsius_to_fahrenheit,numbers))
print(result)


#******************************************filter********************************************************
#remove None values from the list 

list_in_list = [1, None, 3, None, 5]
result = list(filter(None,list_in_list))
print(result)

#extract numbers divisible by 3 using function
def extract_number_divisible_by_3 (numbers):
    return numbers % 3 == 0
   
   
numbers =  [1, 3, 4, 6, 9, 12]
result = list(filter(extract_number_divisible_by_3,numbers))
print(result)

#Use filter() to keep only positive numbers 
def get_positive_numbers(number):
    return number > -1
numbers = [-2,-1, 0, 1, 2]

result = list(filter(get_positive_numbers,numbers))
print(result)

#**********************************DICTIONARY******************************
#select elements from a list of dictionaries 
age = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20}]
def get_age (number):
    return number ["age"] >25


result = list(filter(get_age,age))
print(result)


#***********************************REDUCE************************************************************
#ind the sum of all numbers in the list
from functools import reduce
def add_list_numbers(number,numbers):
    return number+numbers

numbers = [1, 2, 3, 4, 5]
print(reduce(add_list_numbers,numbers))


#write a reduce() function to find the product of all
def multiply_list_numbers(number,numbers):
    return number*numbers
    
numbers = [2, 3, 4]
print(reduce(multiply_list_numbers,numbers))


#find the maximum value in the list
def max_list_numbers(number,numbers):
    return max(number,numbers)
    
numbers = [3, 7, 2, 9, 1]
print(reduce(max_list_numbers,numbers))

#reduce() function to concatenate all strings
def concatenate_name(name,names):
    return name+names

word = ["Hello", " ", "World"]
print(reduce(concatenate_name,word))


#ompute the cumulative sum of squares
def square_list_numbers(number,numbers):
    return number + numbers**2

numb=  [1, 2, 3] 
print(reduce(square_list_numbers,numb))

#sss

def merge_diction (number,numbers):
    number.update(numbers)
    return number

numb=  [{'a': 1},{'b':2} ,{'c':3}]
print(reduce(merge_diction,numb))












