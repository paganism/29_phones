import re
import phonenumbers
from flask import Flask
from models import Orders, db
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)


def normalize_phone(raw_number):
    norm_mob = re.sub(r'(\D+)', '', raw_number)
    try:
        parsed_number = phonenumbers.parse(norm_mob, 'RU')
        if phonenumbers.is_valid_number(parsed_number):
            return parsed_number.national_number
    except NumberParseException:
        return raw_number


def process_order_phones():
    orders = Orders.query.filter_by(
        Orders.normalized_phone_number.is_(None)
    ).order_by(Orders.created.desc()).first()
    normalized_number = normalize_phone(orders.contact_phone)
    orders.contact_phone = normalized_number
    db.session.commit()



if __name__ == "__main__":
    app.run()
