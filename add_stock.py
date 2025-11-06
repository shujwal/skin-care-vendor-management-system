# Import necessary functions from other modules
from read import read_data
from invoice import add_invoice
from invoice import add_new_product_invoice

def add():
    """
    product restocking Function
    
    This function manages inventory restocking by allowing users to:
    - Add quantity to existing products
    - add completely new products to the inventory
    - Generate appropriate invoices for both scenarios
    
    The function updates the inventory in product_data.txt after each addition
    and creates different types of invoices depending on whether existing products
    were restocked or new products were added.
    
    Returns:
        None
    """

    try:
        invoice_list = [] # Stores all items for the current restocking invoice
        s = True
        while s==True:
            products_data = read_data()
            print("Product names:") 
            for i in range(len(products_data)):
                for j in range(len(products_data[i])): 
                    print(f"{i+1}. {products_data[i][0]}")
                    break
            print("="*30)
            print("\nWhich product do you want to add\n Enter the corresponding number or name:")
            product_name = input(">-> ") 
            quantity = int(input("How many would you like to add: "))
            if quantity < 1:
                print("---------------------\nplease enter valid amount!")
                break
            valid = False
            for i in range(len(products_data)):
                if product_name == products_data[i][0] or product_name == str(i+1):
                    # Update quantity of existing product
                    products_data[i][2] = str(int(products_data[i][2]) + quantity)
    
                    name = products_data[i][0]
                    brand = products_data[i][1]
                    unit_price = products_data[i][3]      
                    total_amount = products_data[i][2]           
                    invoice_list_data = [name, brand, quantity, unit_price, total_amount]
                    invoice_list.append(invoice_list_data)
                    # convert 2dlist to 1dlist
                    for i in range(len(products_data)):
                        products_data[i] = ", ".join(products_data[i])
                        products_data[i] +='\n'
                    # Save updated inventory to file
                    with open('product_data.txt','w') as file:
                        file.writelines(products_data) #pass 1dlist
                    print("\nProduct added successfully!\n------------------------------------")
                    valid = True
            if valid == False:
                for i in range(len(products_data)):
                    
                    print("----------------------\nNo product named such is in the store")
                    print("Do you want to add this product to the store?")
                    new = input(">-> ")
                    if new in "YyesYES":
                    # Collect details for the new product
                        new_p_name = product_name
                        new_p_brand = input("Enter the brand: ")
                        new_p_quantity = quantity
                        new_p_price = input("Enter the unit price: ")
                        new_p_country = input("Enter the country where the product was made: ")
                        new_products = f"{new_p_name}, {new_p_brand}, {new_p_quantity}, {new_p_price}, {new_p_country}"
                        new_p_list = new_products.split(", ")
                        products_data.append(new_p_list)
                        invoice_new_p = [new_p_name, new_p_brand, new_p_quantity, new_p_price, new_p_quantity]
                        invoice_list.append(invoice_new_p)
                        for i in range(len(products_data)):
                            products_data[i] = ", ".join(products_data[i])
                            products_data[i] +='\n'
                        # Save updated inventory including new produc
                        with open('product_data.txt','w') as file:
                            file.writelines(products_data) 
                        print("\nProduct added successfully!\n------------------------------------")
                    break    
            conformation = input("-------------------------\nDo you want to continue adding? (Y/N): ")
            if not(conformation == "Y" or conformation == "yes" or conformation == "y"):
                s=False
        # Generate appropriate invoice based on whether existing or new products were added
        if valid == True:
            add_invoice(invoice_list)
        else:
            add_new_product_invoice(invoice_list)   
    except ValueError:
        print("\n---------------------\nError, Please enter valid Quantity\n")
    except:
        print("Error!")