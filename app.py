from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
# Initialize db
db = SQLAlchemy(app)
#Create db model
class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
#Create function to return string when we add something
    def __repr___(self):
        return '<Name %r>' % self.id

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