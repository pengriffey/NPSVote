from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template, redirect,  url_for


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://njmawmcasgapmf:0CVCNvFL4ekB3VWsLK9Kaal_zV@ec2-54-243-212-122.compute-1.amazonaws.com:5432/d5fd58gn4ibb87'


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

@app.route('/nps_results')
def results():
    pr=Votes.query.filter(Votes.hb == "prithvi").count()
    
    return render_template("results.html")
    #return render_template("result.html",result = result)


if __name__ == "__main__":
    db.create_all()
    app.run()
