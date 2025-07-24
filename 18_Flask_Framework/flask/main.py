from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home")
def welcome():
    return render_template('index.html')

@app.route("/")
def hello():
    return "Hello there You are at home page"


if __name__ == "__main__":
    app.run()

