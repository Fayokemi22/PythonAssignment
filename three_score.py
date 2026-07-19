#prompt a user to enter three scores
#calculate the average by dividing the 3 scores with 3
#if the average is >90, average is >80, average is >70, average is >60 print


first_score= int(input("The First Score Is: "))

second_score= int(input("The Second Score is: "))

third_score= int(input("The Third Score is: "))

average = (first_score + second_score + third_score) / 3

if average > 90:
	print(" Excellent: " ,"A")

elif average > 80:
	print(" Verygood: " ,"B")

elif average > 70:
	print(" You Passed: " ,"C")

elif average > 60:
	print(" Average: " ,"D")

else:
	print("Failed")





