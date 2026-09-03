import boto3

def get_product_details(product_id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('products')

    response = table.get_item(
        Key={
            'product_id': product_id
        }
    )

    item = response['Item']
    return item


if __name__ == '__main__':
    product_id = input("Enter the product ID to search for: ")
    try:
        product_details = get_product_details(int(product_id))
        print(f"Product Details:\n{product_details}")
    except Exception as e:
        print(f"NoĬ found with id {product_id}. Error: {e}")
