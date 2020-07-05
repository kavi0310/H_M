import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

# class Stakeholder(db.Document):
#     user_id = db.IntField( max_length=9, unique=True )
#     name    = db.StringField( max_length=30 )
#     password= db.StringField( max_length=15 )

class Staff(db.Document):
    name       =   db.StringField( max_length=30 )
    password   =   db.StringField( max_length=15 )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)

class Registration(db.Document):
    patient_id   =   db.IntField( max_length=9, unique=True)
    patient_name =   db.StringField( max_length=50)
    patient_age  =   db.IntField()
    date_of_join =   db.StringField()
    type_of_bed  =   db.StringField()
    address      =   db.StringField( max_length=200 )
    city         =   db.StringField()
    state        =   db.StringField()

class Medicine(db.Document):
    medicine_name =   db.StringField( max_length=100)
    quantity      =   db.IntField()
    rate          =   db.IntField()
    amount        =   db.IntField()

class Test(db.Document):
    test_name     =   db.StringField( max_length=100 )
    amount        =   db.IntField()
    
class ViewDetails(db.Document):
    medicine_name = db.StringField( max_length=100 )
    test_name     = db.StringField( max_length=100 )
    
