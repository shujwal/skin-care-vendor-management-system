
def read_data():
    """
    read product data from file
    
    This function reads product inventory data from the product_data.txt file
    and processes it into a two-dimensional list format for use in the application.
    
    Each product record is stored as a list with the following structure:
    [name, brand, quantity, price, country_of_origin]
    
    Returns:
        list: A 2D list where each inner list contains data for one product
    """
    with open("product_data.txt", "r") as file:
            products_data = file.readlines() # Read all lines from the file
            for i in range(len(products_data)):
                # Convert each line to a list by stripping whitespace and splitting by commas    
                products_data[i] = products_data[i].strip().split(", ")
    return products_data
