import boto3
import app

#Pulling stock name and daily price from API
stock_name = str(app.api_data.ticker)
stock_price = str(app.api_data.daily_close)

#DynamoDB table name
table_name = "stock_tracker"
dynamodb_client = boto3.client('dynamodb')

stock_info ={
    'Company': {'S': stock_name}
    ,'DailyPrice': {'S': stock_price}
}

print(stock_info)
if __name__ == "__main__":
    
    dynamodb_client.put_item(TableName = table_name, Item = stock_info )