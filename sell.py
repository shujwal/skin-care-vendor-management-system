# Import necessary functions from other modules
from read import read_data
from invoice import sell_invoice


def sell():
    """
    product selling Function
    
    This function handles the sale of products from inventory. It allows users to:
    - select products by name or number
    -specify quantity to sell
    - apply a "buy 2 get 1 free" promotion for quantities over 2
    - Generate sales invoices
    
    The function updates the inventory in product_data.txt after each sale
    and creates an invoice for the transaction using sell_invoice().
    
    Returns:
        None
    """
    try:
        invoice_list = []  # Stores all items for the current invoice
        s = True
        while s==True:
            products_data = read_data()
            print("Product names:") 
            for i in range(len(products_data)):
                for j in range(len(products_data[i])): 
                    print(f"{i+1}. {products_data[i][0]}")
                    break
            print("="*30)
            print("Which product do you want to sell\n Enter the corresponding number or name:")
            product_name = input(">-> ") 
            quantity = int(input("How many would you like to sell: "))
            invoice_valid = False
            if quantity < 1:
                print("---------------------\nplease enter valid amount!")
                break
            product_name_valid = False
            # check if the quantity is 0 or in negative
            if quantity<1:
                print("---------------------------------\nPlease enter valid amount!!")
                break
            for i in range(len(products_data)):
                if product_name == products_data[i][0] or product_name == str(i+1):
                    product_name_valid = True
                    # Calculate free items: 1 free item for every 3 purchased
                    if quantity>2:
                        temp = quantity // 3
                        quantity_after_the_offer = quantity + temp
                        products_data[i][2] = str(int(products_data[i][2]) - quantity_after_the_offer)
                    else:
                        quantity_after_the_offer = quantity
                        products_data[i][2] = str(int(products_data[i][2]) - quantity_after_the_offer)  
                    invoice_valid = True
                    # check if the required stock is greater then available
                    if quantity+quantity_after_the_offer > int(products_data[i][2]):
                        print("-------------------\nplease enter a lower quantity !!, The required amount is greater then available amount") 
                        break      
                    # check if the stock is available        
                    if int(products_data[i][2]) < 1:
                        print("---------------------\nSorry no stock available !!!!\n")
                        break
                    name = products_data[i][0]                  
                    unit_price = products_data[i][3]  
                    invoice_list_data = [name, quantity, quantity_after_the_offer, unit_price]
                    invoice_list.append(invoice_list_data)
                    # convert 2d list to 1d
                    for i in range(len(products_data)):
                        products_data[i] = ", ".join(products_data[i])
                        products_data[i] +='\n'
                        
                    # Update the inventory file with new quantities
                    with open('product_data.txt','w') as file:
                        file.writelines(products_data) #pass 1dlist
                    print("\nProduct Purchased successfully!!\n------------------------------------------")
                    
            if product_name_valid == False :
                print("--------------------------\nPlease enter valid product name\n")
            conformation = input("-------------------------\nDo you want to continue selling? (Y/N): ")
            if not(conformation == "Y" or conformation == "yes" or conformation == "y"):
                s=False
        # Generate an invoice if at least one product was sold
        if invoice_valid == True:
            sell_invoice(invoice_list)
            
    except ValueError:
        print("\n---------------------\nError, Please enter valid input\n")
    except:
        print("Error")
