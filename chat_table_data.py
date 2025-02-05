import boto3

# Create a DynamoDB client configured to use the local endpoint
dynamodb = boto3.client(
    'dynamodb',
    endpoint_url='http://localhost:8000',  # Local DynamoDB endpoint
    region_name='us-east-1',
    aws_access_key_id='local',  # These credentials are for local testing only
    aws_secret_access_key='local'
)

def list_tables():
    """List all tables in local DynamoDB"""
    try:
        response = dynamodb.list_tables()
        print("Tables in local DynamoDB:")
        for table in response['TableNames']:
            print(f"- {table}")
    except Exception as e:
        print(f"Error listing tables: {e}")

def scan_table(table_name):
    """Scan and print all items in a table"""
    try:
        table = boto3.resource(
            'dynamodb',
            endpoint_url='http://localhost:8000',
            region_name='us-east-1',
            aws_access_key_id='local',
            aws_secret_access_key='local'
        ).Table(table_name)
        
        response = table.scan()
        items = response['Items']
        
        print(f"\nItems in table '{table_name}':")
        for item in items:
            print(item)
        print(f"Total items: {len(items)}")
        
    except Exception as e:
        print(f"Error scanning table {table_name}: {e}")


def describe_table(table_name):
    """Describe a specific table's structure"""
    try:
        response = dynamodb.describe_table(TableName=table_name)
        print(f"\nTable structure for '{table_name}':")
        print(response['Table'])
    except Exception as e:
        print(f"Error describing table {table_name}: {e}")

# Use it like this:
# describe_table('Chats')

if __name__ == "__main__":
    # List all tables
    list_tables()
    scan_table('Chats')
    describe_table('Chats')
    
    # You can scan a specific table by uncommenting and modifying the line below
    # scan_table('Chats')  # Replace 'Chats' with your table name