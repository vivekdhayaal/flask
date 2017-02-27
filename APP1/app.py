from flask import Flask, render_template
import json
import pandas as pd

app = Flask(__name__)
app.config.from_pyfile('app_config.cfg')

@app.route('/')
def home():
	return "Welcome to Employee site"

def get_emp_data():
	emp_data = pd.read_csv('employee_details.csv')
	emp_record = emp_data.columns.tolist()
	employees = emp_data.values.tolist()
	return emp_record, employees

@app.route('/employees')
def employees():
    emp_record, employees = get_emp_data()
    return render_template('home.html',emp_rec=emp_record,emp_info=employees)

@app.route('/employeesjson')
def employeesjson():
	emp_record, employees = get_emp_data()
	return json.dumps(employees)

"""
@app.route('/employees/salary')
def salary():
	emp_record, employees = get_emp_data()
	return render_template('salary_cal.html',sal_rec=emp_record,info=employees)
"""

@app.route('/employees/salary')
def salaryavg():
	emp_record, employees = get_emp_data()
	avg = sum(zip(*employees)[-1])/len(employees)
	emp_below_avg = filter(lambda x: x[-1] < avg, employees)
	emp_below_avg_with_name= map(lambda x: x[0], emp_below_avg)
	return render_template('salary_cal.html',avg_sal=avg, emp_below_avg=emp_below_avg_with_name)

if __name__ == '__main__':
    app.run( port=8888)