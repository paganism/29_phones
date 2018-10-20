import re
import phonenumbers
from flask import Flask
from models import Orders, db
from config import Config
from flask_sqlalchemy import SQLAlchemy
from time import sleep
from sqlalchemy.exc import StatementError, OperationalError, InvalidRequestError
import logging
from loggers import logger


app = Flask(__name__)
app.config.from_object(Config)
timeout_check = app.config['CHECK_NEW_ORDERS_TIMEOUT']

db.init_app(app)


def normalize_phone(raw_number):
    digit_number = re.sub(r'(\D+)', '', raw_number)[-10:]
    phonenumbers_suitable_num = '+'.join(digit_number)
    try:
        parsed_number = phonenumbers.parse(phonenumbers_suitable_num, 'RU')
        return parsed_number.national_number
    except phonenumbers.phonenumberutil.NumberParseException:
        return digit_number


def process_order_phones():
    while True:
        try:
            orders = Orders.query.filter(
                Orders.normalized_phone_number.is_(None),
                Orders.contact_phone.isnot(None)
            ).order_by(Orders.created.asc()).first()
            if orders:
                normalized_number = normalize_phone(orders.contact_phone)
                orders.normalized_phone_number = normalized_number
                logger.info(
                    'orders.id=%s with phone %s processed to %s',
                    orders.id,
                    orders.contact_phone,
                    orders.normalized_phone_number)
            db.session.commit()
        except (StatementError, OperationalError, InvalidRequestError) as sqlalchemy_exc:
            db.session.rollback()
            logger.info('database connection problem, rollback')
        sleep(timeout_check)


if __name__ == "__main__":
    with app.app_context():
        process_order_phones()
