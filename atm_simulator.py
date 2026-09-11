
balance = 1000
is_running = True
while(is_running):
    menu = """

     List Of Menu Functions  
    1. deposit
    2. withdraw
    3. check balance
    4. Exit

    """
    print(menu)

    options=int(input("Choose Options"))

    match options:
        case 1:
            amount_to_deposit=float(input("How much are you depositing "))
            balance += amount_to_deposit
            print("You deposited ",amount_to_deposit)
            print("And your balance is",balance)                

        case 2:
            amount_to_withdraw=float(input("How much are you witdrawing "))
            balance -=amount_to_withdraw
            print("You withdrawn ", amount_to_withdraw)
            print("And your balance is ", balance)

        case 3:
            print("Your balance is ",balance)

        case 4:
            is_running = False
            print("Exiting...")

        case _:
            print("Invalid input")
