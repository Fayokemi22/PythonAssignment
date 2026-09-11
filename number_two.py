is_running = True
secret_number = 10

while(is_running):
    number=int(input("Enter Number :"))
    if(number == secret_number):
        print("Correct")
       is_running = False
    if (number > secret_number):
        print("Too High")
    elif number < secret_number:
        print("Too low")
    else:
        print("Wrong")
