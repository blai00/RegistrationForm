from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = 'very secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z\.\+_-]*$')

@app.route('/')
def index(): 
	return render_template("index.html")

@app.route("/process", methods=['Post'])
def validation():
	data = request.form
	print data
	if len(request.form['email'] or request.form['first_name'] or request.form['last_name'] or request.form['password'] or request.form['confirm_password']) < 1:
		flash('One or more field is blank. Please make sure all fields are filled out.')
		return redirect('/')
	if len(request.form['password']) < 8:
		flash("Password needs to be 8 characters long.")
		return redirect('/')
	if not (NAME_REGEX.match(request.form['name']) or NAME_REGEX.match(request.form['last_name'])):
		flash("Invalid Name or Last Name. Please enter a valid name")
		return redirect('/')
	if request.form['password'] != request.form['confirm_password']:
		flash("The passwords don't match.")
		return redirect('/')
	if not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid Email Address. Please enter a valid email.')
		return redirect('/')
	else:
		return render_template("process.html", data=data)

if __name__ == "__main__":
	app.run(debug=True)
		

