# Import necessary functions from other modules
import datetime

def sell_invoice(invoice_data):
    """
    Generate sales invoice
    
    Creates and displays an invoice for products sold to customers, including:
    - special promotional quantities
    - unit and total prices with VAT calculation
    - Customer information
    
    The function saves the invoice to a file and displays it in the console.
    
    returns:
        None
    """
    # Generate unique timestamp for invoice file name
    c_time = str(datetime.datetime.now().hour + datetime.datetime.now().second + datetime.datetime.now().microsecond)
    total_price = 0
    for i in range(len(invoice_data)):
        each_total = int(invoice_data[i][1]) *int(invoice_data[i][3])*2 # Calculate price (quantity * unit_price * 2)
        total_price += each_total
    customer_name = input("Enter customer name: ")
    # Calculate 13% Value Added Tax
    VAT= total_price * 0.13
    with open (f'SELL_product_{c_time}.txt','w') as file:
        file.write(f"Buyer: {customer_name} \n")
        for i in range(len(invoice_data)):
            file.write(f"Product name: {invoice_data[i][0]} || quantity: {invoice_data[i][1]} || quantity gain due to offer: {invoice_data[i][2]} || unit price: {int(invoice_data[i][3])*2} || cost: {int(invoice_data[i][1])*int(invoice_data[i][3])*2}\n")
        
        file.write("Bought from: WeCare vendor\n")
        file.write(f"total cost: {total_price}\n")
        file.write(f"VAT amount: {VAT}\n")
        file.write(f"Grand total cost: {VAT + total_price}")
     
    # Display invoice on console for user confirmation   
    print("-"*20)
    print("INVOICE GENERATED FOR SELLING PRODUCTS\n","-"*20)
    print("Suppliar's name:", customer_name)
    for i in range(len(invoice_data)):
        print(f"Product name: {invoice_data[i][0]}\nquantity ordered: {invoice_data[i][1]}\nquantity gained: {invoice_data[i][2]}\nunit price: {int(invoice_data[i][3])*2}\ncost: {int(invoice_data[i][1])*int(invoice_data[i][3])*2}\n")
        print("-"*5)
    print("Total VAT amount:",VAT)
    print("Grand Total:",int(VAT)+int(total_price),"\n"+"-"*20)

def add_invoice(invoice_data):
    """
    Generate restocking invoice for existing products
    
    Creates and displays an invoice for restocking existing products, including:
    - Quantity and cost information
    - Supplier details and transaction date
    - Current inventory after restocking
    
    The function saves the invoice to a file and displays it in the console.
    
    returns:
        None
    """
    
    # Generate unique timestamp for invoice file name
    c_time = str(datetime.datetime.now().hour + datetime.datetime.now().second + datetime.datetime.now().microsecond)
    total_price = 0
    for i in range(len(invoice_data)):
        # Calculate total cost (quantity * unit_price)
        each_total = int(invoice_data[i][2]) *int(invoice_data[i][3])
        total_price += each_total
    
    supplier_name = input("Enter Supplier name: ")
    date_of_trans = input("Enter the date of transaction: ")
    with open (f'ADD_product_{c_time}.txt','w') as file:
        for i in range(len(invoice_data)):
            file.write(f"Product name: {invoice_data[i][0]} || brand: {invoice_data[i][1]} || quantity: {invoice_data[i][2]} || unit price: {(invoice_data[i][3])} || cost: {int(invoice_data[i][2])*int(invoice_data[i][3])} || Currently available: {invoice_data[i][4]} \n")
            
        file.write(f"Suppliar: {supplier_name}\n")
        file.write(f"Date of restock: {date_of_trans}\n")
        file.write(f"Grand total cost: {total_price}\n--------------------------------\n")
     
    # Display invoice on console for user confirmation   
    print("-"*20)
    print("INVOICE GENERATED FOR PRODUCTS RESTOCK\n","-"*20)
    print("Suppliar's name:", supplier_name)
    print("Date of transaction:", date_of_trans)
    print("-"*5)
    for i in range(len(invoice_data)):
        print(f"Product name: {invoice_data[i][0]}\nbrand: {invoice_data[i][1]}\nquantity: {invoice_data[i][2]}\nunit price: {(invoice_data[i][3])}\ncost: {int(invoice_data[i][2])*int(invoice_data[i][3])}\n")
        print("-"*5)
    print("Grand Total:", total_price,"\n"+"-"*20)
    
    
def add_new_product_invoice(invoice_data):
    """
    Generate invoice for new products addition
    
    Creates and displays an invoice for adding new products to inventory, including:
    - Product details and costs
    - Supplier information and transaction date
    - Initial inventory quantity
    
    The function saves the invoice to a file and displays it in the console.
    
    returns:
        None
    """
    
    # Generate unique timestamp for invoice file name    
    c_time = str(datetime.datetime.now().hour + datetime.datetime.now().second + datetime.datetime.now().microsecond)
    total_price = 0
    for i in range(len(invoice_data)):
        # Calculate total cost (quantity * unit_price)
        each_total = int(invoice_data[i][2]) *int(invoice_data[i][3])
        total_price += each_total
    
    supplier_name = input("Enter Supplier name: ")
    date_of_trans = input("Enter the date of transaction: ")
    with open (f'ADD_new_product_{c_time}.txt','w') as file:
        for i in range(len(invoice_data)):
            file.write(f"Product name: {invoice_data[i][0]} || brand: {invoice_data[i][1]} || quantity: {invoice_data[i][2]} || unit price: {(invoice_data[i][3])} || cost: {int(invoice_data[i][2])*int(invoice_data[i][3])} || Currently available: {invoice_data[i][4]} \n")
            
        file.write(f"Suppliar: {supplier_name}\n")
        file.write(f"Date of restock: {date_of_trans}\n")
        file.write(f"Grand total cost: {total_price}\n--------------------------------\n")
    # Display invoice on console for user confirmation    
    print("-"*20)
    print("INVOICE GENERATED FOR NEW PRODUCTS ADDED\n","-"*20)
    print("Suppliar's name:", supplier_name)
    print("Date of transaction:", date_of_trans)
    print('-'*5)
    for i in range(len(invoice_data)):
        print(f"Product name: {invoice_data[i][0]}\nbrand: {invoice_data[i][1]}\nquantity: {invoice_data[i][2]}\nunit price: {(invoice_data[i][3])}\ncost: {int(invoice_data[i][2])*int(invoice_data[i][3])}\n")
        print("-"*5)
    print("Grand Total:", total_price,"\n"+"-"*20)