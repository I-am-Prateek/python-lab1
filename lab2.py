#defining the global variable 
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

#defining a function to count a dollar
def dollar_count():
    pennie=int(input("Enter the number of pennies:"))
    nickels=int(input("Enter the number of nickels:"))
    dimes=int(input("Enter the number of dimes:"))
    quarters=int(input("Enter the number of quarters:"))

    #calculating the total value entered by user

    total_cent=(pennie*PENNY_VALUE)+ (nickels*NICKEL_VALUE) + (dimes*DIME_VALUE)+ (quarters*QUARTER_VALUE)

    total_dollars= (total_cent/PENNIES_IN_DOLLAR)

    #applying the necessary conditions

    if total_dollars>1:
        print("Sorry, the amount you entered was more than one dollar.")
    elif total_dollars<1:
        print("Sorry, the amount you entered was less than one dollar.")
    else:
        print("Congratulations!The amount you entered was exactly one dollar! You win the game!")

dollar_count()
    
