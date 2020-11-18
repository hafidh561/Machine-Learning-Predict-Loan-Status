from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class DataForm(FlaskForm):
	gender = SelectField('Gender', choices=[(1, 'Male'), (0, 'Female')], validators=[DataRequired()])
	married = SelectField('Married', choices=[(1, 'Yes'), (0, 'No')], validators=[DataRequired()])
	dependents = SelectField('Dependents', choices=[(0, '0'), (1, '1'),
	                                                (2, '2'), (3, '3+')], validators=[DataRequired()])
	education = SelectField('Education', choices=[(1, 'Graduate'), (0, 'Not Graduate')], validators=[DataRequired()])
	self_employed = SelectField('Self Employed', choices=[(1, 'Yes'), (0, 'No')], validators=[DataRequired()])
	applicant_income = IntegerField('Applicant Income', validators=[DataRequired()])
	coapplicant_income = IntegerField('Coapplicant Income', validators=[DataRequired()])
	loan_amount = IntegerField('Loan Amount', validators=[DataRequired()])
	loan_amount_term = IntegerField('Loan Amount Term', validators=[DataRequired()])
	credit_history = SelectField('Credit History', choices=[(0, '0'), (1, '1')], validators=[DataRequired()])
	property_area = SelectField('Property Area', choices=[(0, 'Urban'), (1, 'Rural'), (2, 'Semiurban')],
	                            validators=[DataRequired()])
	submit = SubmitField('Submit')
