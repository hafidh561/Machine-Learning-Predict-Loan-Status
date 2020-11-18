import pickle

import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model


def predict_input(gender, married, dependents, education, self_employed,
                  applicant_income, coapplicant_income, loan_amount,
                  loan_amount_term, credit_history, property_area):

	with open('scaler', 'rb') as f:
		scaler = pickle.load(f)

	model = load_model('loan_model.h5')

	df_input = pd.DataFrame({
		'gender': [int(gender)],
		'married': [int(married)],
		'dependents': [int(dependents)],
		'education': [int(education)],
		'self_employed': [int(self_employed)],
		'applicant_income': [applicant_income],
		'coapplicant_income': [coapplicant_income],
		'loan_amount': [loan_amount],
		'loan_amount_term': [loan_amount_term],
		'credit_history': [int(credit_history)],
		'property_area': [int(property_area)]
	})

	df_input.iloc[:, 5:9] = scaler.transform(df_input.iloc[:, 5:9])
	result = np.argmax(model.predict(df_input), axis=-1)

	if result == 0:
		return "No, you can't!"
	elif result == 1:
		return "Yes, you can!"
