#Идрисова Лена 368234, вариант 4
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///steps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Steps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(60), nullable=False)
    number = db.Column(db.Integer, nullable=False)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        number = request.form['number']
        data_steps = Steps(date=date, number=number)
        db.session.add(data_steps)
        db.session.commit()
        return redirect(url_for('index'))
    all_number = Steps.query.all()
    return render_template('index.html', steps=all_number)


@app.route('/clear', methods=['POST'])
def clear():
    db.session.query(Steps).delete()
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)