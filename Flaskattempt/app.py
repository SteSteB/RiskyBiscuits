from flask import Flask, render_template
app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

@app.route("/")
def home():
    return render_template("index.html")

# New functions
@app.route("/aboutus/")
def aboutus():
    return render_template("aboutus.html")

@app.route("/contactus/")
def contactus():
    return render_template("contactus.html")

@app.route("/qa/")
def qa():
    return render_template("qa.html")

@app.route("/week1/")
def week1():
    return render_template("week1.html")

@app.route("/week2/")
def week2():
    return render_template("week2.html")

@app.route("/week3/")
def week3():
    return render_template("week3.html")

@app.route("/week4/")
def week4():
    return render_template("week4.html")

@app.route("/week5/")
def week5():
    return render_template("week5.html")

@app.route("/kanban")
def kanban():
    return render_template("kanban.html")

@app.route("/oscar")
def oscar():
    return render_template("oscar.html")

@app.route("/requirements")
def requirements():
    return render_template("requirements.html")

@app.route("/threatmodelling")
def threatmodelling():
    return render_template("threatmodelling.html")
    

@app.route("/stride")
def stride():
    return render_template("stride.html")


