from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def embedexample():
    return render_template('embed.html')

if __name__ == '__main__':
    app.run(debug=True)