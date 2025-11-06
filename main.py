# Import necessary functions from other modules
from read import read_data
from sell import sell
from add_stock import add

"""
Store Inventory Management System

This program provides a command-line interface for managing store inventory.
It allows users to view products, sell items, restock inventory, and exit the system.
The program runs in a loop until the user chooses to exit.

functions:
    main(): Displays the menu and handles user input for inventory operations
"""
def main():
    '''
    This method display the menu and also handles the user's input for different operations
    it allows user to
    - view all product details, when entering 1 or 'view'
    - sell available products, when entering 2 or 'sell'
    - restock available product as well as new products if needed, when entering 3 or 'restock'
    - exit the shop, when entering 4 or 'exit'
    
    returns:
        none
    '''
    # Display the main menu options to the user
    print("Welcome")
    print("Enter 1 or 'view' for viewing the products")
    print("Enter 2 or 'sell' for selling products")
    print("Enter 3 or 'restock' for buying products")
    print("Enter 4 or 'exit' for exiting the store")
    option = input("-> ")

    match option.strip():
        case "1" | "view" | "VIEW" | "View":
            products_data = read_data()
            # Display the product details
            print("===== Available Products =====")
            for i in range(len(products_data)):
                for j in range(len(products_data[i])):
                    if j==0:
                        print("Name:",products_data[i][j])
                    if j==1:
                        print("Company:",products_data[i][j])
                    if j==2:
                        print("Quantity:",products_data[i][j])
                    if j==3:
                        # Display selling price (cost price * 2)
                        print("Price:",int(products_data[i][j])*2)
                    if j==4:
                        print("Made in:",products_data[i][j])
                print("="*30) 
                   
        case "2" | "sell" | "Sell" | "SELL":
            sell()                
            
        case "3" | "restock" | "Restock" | "RESTOCK":
            add()
                
        case "4" | "Exit" | "EXIT":
            print("------------------\nThank You!!")
            
        case _:
            print("Please input numbers between 1 and 4")
            
# Main program loop that continues as user commands
choose = True
while choose == True:
    main()
    choice_negative = "NOno"
    choice_positive = "YESyes"
    second_choose = False
    while second_choose == False:
        choice = input("-------------------------------------------------\nDo you want to continue your activities in the shop? \n Yes/No: ")
        if choice in choice_negative:
            second_choose = True
            choose = False
        elif choice in choice_positive:
            second_choose = True
            choose = True
        else:
            print("-----------------------------\nPlease enter valid input")
            second_choose = False  
 
