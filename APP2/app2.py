from flask import Flask, request, render_template
from db_schema import insert_emp_record
app2 = Flask(__name__)

@app2.route("/register",methods=['POST','GET'])
def register():
	message=""
	if request.method == "POST":
		data = request.form
		result = insert_emp_record(data)
		if result :
			message = "Employee inserted successfully"
	return render_template("register.html", message=message)

	

@app2.route("/createemp",methods=['POST'])
def emp_create():
	data = request.json
	emp_record = insert_emp_record(data)
	if emp_record:
		return "Employee created successfully"
	else:
		return "Employee not created"


if __name__ == "__main__":
  app2.run(port=8888,debug=True)
