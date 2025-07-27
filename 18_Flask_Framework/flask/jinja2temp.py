from flask import Flask, render_template, request ,redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello there! You are at the home page."

@app.route("/home", methods=['GET'])
def welcome():
    return render_template('index.html')

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

# Variable Rule
# @app.route("/success/<score>")
@app.route("/success/<int:score>") #### Invalid
def success(score):
    res=""
    if score>35:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',results=res)


@app.route("/result/<int:score>") #### Invalid
def result_new(score):
    res=""
    if score>35:
        res="PASS"
    else:
        res="FAIL"
    exp={'Score':score,"Results":res}
    return render_template('result1.html',results=exp)
    # return f"Hii You got {score} Marks "

@app.route('/score/<int:score>')
def score(score):
    return render_template('score.html',score=score)

@app.route('/totalscore',methods=['GET','POST'])
def totalscore():
    totalscore=0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        totalscore=(science+data_science+maths+c)/4

    return redirect(url_for('score',score=totalscore))


if __name__ == "__main__":
    app.run(debug=True)
