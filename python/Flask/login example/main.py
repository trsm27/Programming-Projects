from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)

@app.route('/')
def home():
    return "login successful"


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            #execute what to do if the user has failed to log in
            error = 'Invalid Credentials. Please try agin'
            print("login failed")
        else:
            print("successfully logged in!")
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)