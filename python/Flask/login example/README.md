# Login Example
	to add a login function to your website insert this snippet as a new route:
		@app.route('/login', methods=['GET', 'POST']) #1
		def login():
			error = None
			if request.method == 'POST':
				if request.form['username'] != 'admin' or request.form['password'] != 'admin':
					error = 'Invalid Credentials. Please try again.'
					print("login failed!")
				else:
					print("you have successfully logged in!")
			return render_template('login.html', error=error)
	
1. Specified the applicable HTTP methods for the route, GET and POST, as an argument in the route decorator.
   For the new /login route we need to specifiy the POST method as well as GET so that end users can send a POST request with their login credentials to that /login endpoint.
	The login() function tests to see if the credentials are correct. If they are correct, then python will output that the user has successfully logged in and if the credentials are incorrect, an error populates and python will also output that the login failed. The credentials come from the POST request

In the case of a GET request, the login page is simply rendered.