from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError
from Yellow.models import Record
import phonenumbers

StateList = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 
'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 
'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
  'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
   'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
choices =[]
for state in StateList:
    choices.append((state, state))

class RecordForm(FlaskForm):
    companyname = StringField('Company Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', choices = choices)
    zip = StringField('Zip', validators=[DataRequired()])
    phone = StringField('Phone')

    submit = SubmitField('Create Account')

    def validate_phone(self, phone):
        if len(phone.data) == 10:
            try:
                myNum = phonenumbers.parse(phone.data, "US")
            except Exception:
                raise ValidationError('The input was not a valid US number. Must be a real number and 10 digits long.')
            print(myNum)
            if phonenumbers.is_valid_number(myNum) == False:
                raise ValidationError('The input was not a valid US number. Must be a real number and 10 digits long.')
        else:
            raise ValidationError('The input was not a valid US number. Must be a real number and 10 digits long.')