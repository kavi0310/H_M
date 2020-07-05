from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, length, ValidationError
from application.models import Staff , Registration , Medicine , Test

class LoginForm(FlaskForm):
    name        = StringField("Username", validators=[DataRequired(message="Enter Username")])
    password    = StringField("Password", validators=[DataRequired(message="Enter Password")])
    remember_me = BooleanField("Remember Me")
    submit      = SubmitField("Login")

class PatientRegForm(FlaskForm):
    patient_id     = IntegerField("Patient ID", validators=[DataRequired(message="Should be in Numerical data formate")])
    patient_name   = StringField("Patient Name", validators=[DataRequired(message="Should be in String formate")])
    patient_age    = IntegerField("Patient Age", validators=[DataRequired(message="Should be in Numerical data formate")])
    date_of_join   = StringField("Date_of_join", validators=[DataRequired(message="Enter valid date")])
    type_of_bed    = SelectField("Type_of_bed", choices = [('Select Bed','Select'),('General ward','General ward'),('Semi sharing','Semi sharing'),('Single room','Single room')], validators=[DataRequired()])
    address        = StringField("Address", validators=[DataRequired(message="Enter valid address")])
    city           = SelectField("City", choices = [('Select City','Select'),('Erode','Erode'),('Ooty','Ooty'),('Chennai','Chennai'),('Coimbatore','Coimbatore'),('Selam','Selam'),('Karur','Karur'),('Namakkal','Namakkal')], validators=[DataRequired()])
    state          = SelectField("State", choices = [('Select State','Select'),('Tamil Nadu','Tamil Nadu'),('Karnadaga','Karnadaga'),('Kerala','Kerala')], validators=[DataRequired()])
    submit         = SubmitField("Register Now")

    def validate_patient_id(self,patient_id):
        registration = Registration.objects(patient_id=patient_id.data).first()
        if registration:
            raise ValidationError("Patient ID is Already in use, Try again")

class PatientUpdateForm(FlaskForm):
    patient_id     = IntegerField("Patient ID", validators=[DataRequired(message="Should be in Numerical data formate")])
    patient_name   = StringField("Patient Name", validators=[DataRequired(message="Should be in String formate")])
    patient_age    = IntegerField("Patient Age", validators=[DataRequired(message="Should be in Numerical data formate")])
    date_of_join   = StringField("Date_of_join", validators=[DataRequired(message="Enter valid date")])
    type_of_bed    = SelectField("Type_of_bed", choices = [('Select Bed','Select'),('General ward','General ward'),('Semi sharing','Semi sharing'),('Single room','Single room')], validators=[DataRequired()])
    address        = StringField("Address", validators=[DataRequired(message="Enter valid address")])
    city           = SelectField("City", choices = [('Select City','Select'),('Erode','Erode'),('Ooty','Ooty'),('Chennai','Chennai'),('Coimbatore','Coimbatore'),('Selam','Selam'),('Karur','Karur'),('Namakkal','Namakkal')], validators=[DataRequired()])
    state          = SelectField("State", choices = [('Select State','Select'),('Tamil Nadu','Tamil Nadu'),('Karnadaga','Karnadaga'),('Kerala','Kerala')], validators=[DataRequired()])
    submit         = SubmitField("Update Now")
   

class MedicineForm(FlaskForm):
    medicine_name  = StringField("Medicine Name", validators=[DataRequired()])
    quantity       = IntegerField("Quantity", validators=[DataRequired()])
    rate           = IntegerField("Rate",  validators=[DataRequired()])
    amount         = IntegerField("Amount",  validators=[DataRequired()])
    submit         = SubmitField("Update")

class TestForm(FlaskForm):
    test_name  = StringField("Medicine Name", validators=[DataRequired()])
    amount         = IntegerField("Amount",  validators=[DataRequired()])
    submit         = SubmitField("Update")