from flask import Flask

app = Flask(__name__)

@app.route("/home")
def welcome():
    print("Welcome route triggered")  # debug print
    return "Welcome to the Flask app"

@app.route("/")
def hello():
    return "Hello there You are at home page"


if __name__ == "__main__":
    app.run()

