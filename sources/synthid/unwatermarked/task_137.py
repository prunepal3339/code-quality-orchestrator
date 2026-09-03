import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

def get_product_details(product_id):
    """
    Fetches product details from the database based on the product ID.
    
    :param product_id: The ID of the product to fetch details for.
    :return: A tuple containing the product details or None if no product is found.
    """
    query = "SELECT id, name, price, description FROM product_table WHERE id = ?"
    cursor.execute(query, (product_id,))
    result = cursor.fetchone()
    return result

def main():
    while True:
        # Get user input
        try:
            product_id = int(input("Enter the product ID to inquire about (or 'q' to quit): "))
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'q'.")
            continue
        
        if product_id == 'q':
            print("Exiting the program.")
            break
        
        # Retrieve product details
        product_details = get_product_details(int(product_id))
        
        if product_details:
            print(f"Product ID: {product_details[0]}")
            print(f"name: {product-details[1]}")
            price = f"${product_details[2]:.2f}"
            print(f_price: {price}")
            print(f"description: {product_Details[3]}")
        else:
            print("\nNo product found with the given ID.\n")

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
