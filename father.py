# prompt users to enter 2 integer
#Current  father's age (years)
#current age of his son (years)
# father's years ago is ( multiply son's age twice)




father_age =int (input ("Current Father's Age: "))

son_Age = int (input("Current Son's Age: "))

years = father_age - (son_Age * 2)

if years>0 or  years == 0:

	print("The father would be twice older than his son in", years , "years")

