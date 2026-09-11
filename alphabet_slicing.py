alphabet_slicing='abcdefghijklmnopqrstuvwxyz'

#the half of the alphabet

first_half = alphabet_slicing[0:13]
print(f"The first half is {first_half} ")

#The first half of the string using only the ending index.

ending_index = alphabet_slicing[:13]
print(f"The ending index  is {ending_index} ")

#The second half of the string using starting and ending indices.

second_half = alphabet_slicing[13:26]
print(f"The ending index  is {second_half} ")

#The second half of the string using only the starting index.

starting_index = alphabet_slicing[13:]
print(f"The ending index  is {starting_index} ")

#Every second letter in the string starting with 'a'.

every_second_letter = alphabet_slicing[::2]
print(f"The letters are: {every_second_letter}")

#The entire string in reverse.

reverse_entire_letter = alphabet_slicing[-1: :-1]
print(f"The reverse : {reverse_entire_letter} ")

#Every third letter of the string in reverse starting with 'z'


reverse_every_three_letters_from_z = alphabet_slicing[-1: :-3]
print(f"Every three reverse : {reverse_every_three_letters_from_z} ")
