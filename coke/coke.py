# Variable to keep track
amount_due = 50

#Loop until amount_due is greater than 0
while amount_due > 0:

    #Print the amount_due
    print("Amount Due: ", amount_due)
    
    # Ask user to insert coin 
    coin = int(input("Insert Coin: "))

    # Check if coin is 25, 10  or 5 cents
    if coin in [25, 10, 5]:

        #Substract value from amont_due
        amount_due -= coin
        
#Caclculate change_owed
change_owed = abs(amount_due)

#Print the result
print("Change Owed: ", change_owed)
