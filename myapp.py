from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template, redirect,  url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
app.debug=True


class Votes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hg = db.Column(db.String(80))
    hb = db.Column(db.String(120))

    def __init__(self,hg, hb):
        self.hg = hg
        self.hb = hb

    def __repr__(self):
        return '<User %r>' % self.hb


@app.route('/')
def index():
    return render_template('vote.html')


@app.route('/nps_vote', methods=['POST'])
def post_user():
    vote = Votes(request.form['hg'], request.form['hb'])
    db.session.add(vote)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()