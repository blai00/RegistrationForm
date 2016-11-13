from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = 'very secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z\.\+_-]*$')

@app.route('/')
def index(): 
	return render_template("index.html")

@app.route("/process", methods=['POST'])
def validation():
	
	data = request.form
	print data
	if not request.form['first_name']:
		flash('Plese enter a name')
		return redirect('/')
	elif len(request.form['first_name']) < 2 :
		flash('Your first name needs to be longer than 2 characters.')
		return redirect('/')
	if not request.form['email']:
		flash('Please enter an email address.')
		return redirect('/')
	elif len(request.form['email']) < 2:
		flash('Your email has to be longer than 2 characters')
		return redirect('/')
	if not request.form['last_name']:
		flash('Plese enter a last name')
		return redirect('/')
	elif len(request.form['last_name']) < 1 :
		flash('Your last name needs to be longer than 1 character.')
		return redirect('/')
	if not request.form['password']:
		flash('Please enter a password.')
		return redirect('/')
	elif len(request.form['password']) < 8:
		flash("Password needs to be 8 characters long.")
		return redirect('/')
	if not (NAME_REGEX.match(request.form['first_name']) or NAME_REGEX.match(request.form['last_name'])):
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
		

