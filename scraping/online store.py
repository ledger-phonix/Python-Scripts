print("Online Store")
print('Buy Items')
print("-------------------------------------------")
# Here is the prices of three items called p1 p2 and p3.
P1 = 200.0
P2 = 400.0
P3 = 600.0
#I display all in items available in online store alonge prices and combo deals.
print("Product(s) \t\t Prices")
print("[0] Item 1 \t\t ", P1)
print("[1] Item 2 \t\t ", P2)
print("[2] Item 3 \t\t ", P3)
print("[3] combo 1 (Item 1 + 2) ")
print("[4] combo 2 (Item 2 + 3)  ")
print("[5] combo 3 (Item 1 + 3)  ")
print("[6] combo 4 (Item 1 + 2 + 3) ")
print("-------------------------------------")

# Here is the variable which will take the integer values from the user.
choice = int(input('Choose a product number from 0 to 6:  '))

# I created a  function in here named selection, with the parameter which is choice. 
def selection(choice):
    #I used if statement in this function and performed calculations on combo deals.
    if choice == 0:
        print("your payable amout is :",P1) 
    elif choice == 1:
        print("Your payable amount is :",P2)
    elif choice == 2:
        print("Your payable amount is :",P3)
    elif choice == 3:
        disc1 = (P1+P2)* 0.1
        print("Your Total amount is: " , P1+P2, "\nYou got 10% diccount: ",disc1,"\nYour Payable amount is:", (P1+P2)-disc1)
    elif choice == 4:
        disc1 = (P2+P3)* 0.1
        print("Your Total amount is: " , P2+P3, "\nYou got 10% diccount: ",disc1,"\nYour Payable amount is:", (P2+P3)-disc1)
    elif choice == 5:
        disc1 = (P1+P3)* 0.1
        print("Your Total amount is: " , P1+P3, "\nYou got 10% diccount: ",disc1,"\nYour Payable amount is:", (P1+P3)-disc1)     
    elif choice == 6:
        disc1 = (P1+P3+P2)* 0.25
        print("Your Total amount is: " , P1+P3+P2, "\nYou got 25% diccount: ",disc1,"\nYour Payable amount is:", (P1+P3+P2)-disc1) 
        # If a user chose anyother number which is not available in list. It will display invalid number.
    else:
        print("Enter a valid number.")   
# Here i called the fuction.
selection(choice)