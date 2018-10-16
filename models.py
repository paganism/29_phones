from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, index=True)
    contact_phone = db.Column(db.String(100))
    normalized_phone_number = db.Column(db.String(20))
