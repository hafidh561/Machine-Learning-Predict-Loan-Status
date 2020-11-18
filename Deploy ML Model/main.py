from flask import Flask, render_template

from forms import DataForm
from model import predict_input

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a1ce5f730439a2109184f2e515b9e484'


@app.route('/', methods=['GET', 'POST'])
def index():
	form = DataForm()
	if form.validate_on_submit():
		gd = form.gender.data
		md = form.married.data
		dp = form.dependents.data
		ed = form.education.data
		se = form.self_employed.data
		apl = form.applicant_income.data
		coapl = form.coapplicant_income.data
		la = form.loan_amount.data
		lat = form.loan_amount_term.data
		ch = form.credit_history.data
		pa = form.property_area.data
		result = predict_input(gd, md, dp, ed, se, apl, coapl, la, lat, ch, pa)
		return render_template('index.html', form=form, title='Predict Loan Status', result=result)
	else:
		return render_template('index.html', form=form, title='Predict Loan Status', result='')


if __name__ == '__main__':
	app.run()
