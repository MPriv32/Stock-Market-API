import boto3
import os
import requests


url = (
    'https://api.polygon.io/v1/open-close/{stock}/2020-10-14?adjusted=true&apiKey={API_key}'
)

if os.path.isfile('.env'):
    from dotenv import load_dotenv
    load_dotenv()

response = requests.get(url.format(
    stock=os.getenv('stock'),
    API_key=os.getenv('API_key')
))

#Pulling stock name and daily price from API
data = response.json()
stock_name = str(data['symbol'])
price = str(data['close'])

table_name = "stock_tracker"

dynamodb_client = boto3.client('dynamodb')

stock_info ={
    'Company': {'S': stock_name}
    ,'DailyPrice': {'S': price}
}

print(stock_info)
if __name__ == "__main__":
    
    dynamodb_client.put_item(TableName = table_name, Item = stock_info )