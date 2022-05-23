import boto3
import app
import os

#Pulling stock name and daily price from API
stock_name = str(app.api_data.ticker)
stock_price = str(app.api_data.daily_close)

if os.path.isfile('.env'):
    from dotenv import load_dotenv
    load_dotenv()

ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

#DynamoDB table name
table_name = "stock_tracker"
dynamodb_client = boto3.client('dynamodb', region_name='us-west-2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

stock_info ={
    'Company': {'S': stock_name}
    ,'DailyPrice': {'S': stock_price}
}

print(stock_info)


if __name__ == "__main__":
    
    dynamodb_client.put_item(TableName = table_name, Item = stock_info )
