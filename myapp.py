from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template, redirect,  url_for
from flask_basicauth import BasicAuth


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://njmawmcasgapmf:0CVCNvFL4ekB3VWsLK9Kaal_zV@ec2-54-243-212-122.compute-1.amazonaws.com:5432/d5fd58gn4ibb87'

app.config['BASIC_AUTH_USERNAME'] = '123'
app.config['BASIC_AUTH_PASSWORD'] = '123'
basic_auth = BasicAuth(app)

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
def vote():
    pw=""
    return render_template('vote.html')
    return pw

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


@app.route('/nps_vote', methods=['POST'])
def post_user():
    vote = Votes(request.form['hg'], request.form['hb'])
    db.session.add(vote)
    db.session.commit()
    return redirect(url_for('thanks'))


@app.route('/nps_results')
@basic_auth.required
def results():
        prithvi=Votes.query.filter(Votes.hb == "prithvi").count()
        tanush=Votes.query.filter(Votes.hb == "tanush").count()
        sneha=Votes.query.filter(Votes.hg == "sneha").count()
        neha=Votes.query.filter(Votes.hg == "neha").count()

        print("Total Voters",(sneha + neha))

        results={"Prithvi":prithvi,"Tanush":tanush,"Sneha":sneha,"Neha":neha}


        return render_template("results.html", results=results)
        #return render_template("result.html",result = result)


if __name__ == "__main__":
    db.create_all()
    app.run()
