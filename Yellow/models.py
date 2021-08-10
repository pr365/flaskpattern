from datetime import datetime
from Yellow import db

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyname = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    city = db.Column(db.String(50), unique=False, nullable=False)
    state = db.Column(db.String(50), unique=False, nullable=False)
    zip = db.Column(db.String(10), unique=False, nullable=False)
    phone = db.Column(db.String(16), unique=False, nullable=False)

    def __repr__(self):
        return f"Record('{self.companyname}', '{self.email}', '{self.phone}')"
