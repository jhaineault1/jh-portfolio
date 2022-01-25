from flask import Flask, render_template

app = Flask(__name__)

#flask route for each tab
@app.route('/')
def index():
    title = "Jeff Haineault's Portfolio"
    return render_template("index.html", title=title)

@app.route('/about')
def about():
    names = ["Jeff", "Mack", "Hain"]
    return render_template("about.html", names=names)

@app.route('/projects')
def projects():
    return render_template("projects.html")
