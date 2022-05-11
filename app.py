from datetime import datetime
import smtplib
import os
import requests

today_date = {datetime.today().strftime("%Y-%m-%d")}


url = (
    'https://api.polygon.io/v1/open-close/{stock}/2022-05-10?adjusted=true&apiKey={API_key}'
)

if os.path.isfile('.env'):
    from dotenv import load_dotenv
    load_dotenv()

def __send_email(stock_data: str) -> None:
    gmail_user = os.getenv('EMAIL_USER')
    gmail_password = os.getenv('EMAIL_PASSWORD')

    mail_from = gmail_user
    mail_to = gmail_user

    mail_subject = f'Your stock update for {datetime.today().strftime("%m/%d/%Y")}'
    mail_message = f'Subject: {mail_subject}\n\n{stock_data}'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(mail_from, mail_to, mail_message)
    server.close()

class api_data:
    response = requests.get(url.format(
        stock=os.getenv('stock'),
        API_key=os.getenv('API_key')
    ))

    data = response.json()
    ticker = data['symbol']
    daily_high = data['high']
    daily_low = data['low']
    daily_close = data['close']

def __email_body():

    stock_data = (
        f"""For the stock: {api_data.ticker}
        \nToday's high was {api_data.daily_high}
        \nToday's low was $ {api_data.daily_low} 
        \n{api_data.ticker} closed at $ {api_data.daily_close}"""
    )

    __send_email(stock_data)

__email_body()
