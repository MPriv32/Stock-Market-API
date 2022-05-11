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

def handler(event, context):
    response = requests.get(url.format(
        stock=os.getenv('stock'),
        API_key=os.getenv('API_key')
    ))

    data = response.json()
    stock_data = (
        "For the stock: " + str(data['symbol']) +
        "\nToday's high was $" + str(data['high']) +
        "\nToday's low was $" + str(data['low']) + "\n" + 
        str(data['symbol']) +  " closed at $" + str(data['close'])
    )

    __send_email(stock_data)

handler(None, None)
