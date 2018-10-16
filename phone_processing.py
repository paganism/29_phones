import re
import phonenumbers 
from flask import Flask
from models import Orders, db
from config import Config
from flask_sqlalchemy import SQLAlchemy
from time import sleep


app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)


def normalize_phone(raw_number):
    digit_number = re.sub(r'(\D+)', '', raw_number)[-10:]
    try:
        parsed_number = phonenumbers.parse(digit_number, 'RU')
        return parsed_number.national_number
    except phonenumbers.phonenumberutil.NumberParseException:
        return digit_number


def process_order_phones():
    while True:
        orders = Orders.query.filter(
            Orders.normalized_phone_number.is_(None),
            Orders.contact_phone.isnot(None)
        ).order_by(Orders.created.asc()).first()
        if orders:
            normalized_number = normalize_phone(orders.contact_phone)
            orders.normalized_phone_number = normalized_number
        db.session.commit()
        sleep(app.config['CHECK_NEW_ORDERS_TIMEOUT'])


if __name__ == "__main__":
    with app.app_context():
        process_order_phones()
