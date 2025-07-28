from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello there! You are at the home page."

@app.route("/home", methods=['GET'])
def welcome():
    return render_template('index.html')

# @app.route("/form", methods=['GET', 'POST']) 
# @app.route("/form", methods=['GET', 'POST']) 
@app.route("/form", methods=['GET', 'POST']) 
def form():
    if request.method == 'POST':
        name = request.form.get("name")
        return f"Form submitted! Name: {name}"
    return render_template('form.html')

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form.get('name')
        return f"{name} form submitted successfully !!"
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
