from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam_app.db'
db = SQLAlchemy(app)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    option1 = db.Column(db.String(100), nullable=False)
    option2 = db.Column(db.String(100), nullable=False)
    option3 = db.Column(db.String(100), nullable=False)
    option4 = db.Column(db.String(100), nullable=False)
    correct_option = db.Column(db.String(100), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    highest_score = db.Column(db.Integer, default=0)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/exam')
def exam():
    questions = Question.query.all()
    return render_template('exam.html', questions=questions)


@app.route('/submit', methods=['POST'])
def submit():
    questions = Question.query.all()
    score = 0
    for question in questions:
        selected_option = request.form.get(str(question.id))
        if selected_option == question.correct_option:
            score += 1

    if 'user_id' not in session:
        user = User(highest_score=score)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
    else:
        user = User.query.get(session['user_id'])
        if score > user.highest_score:
            user.highest_score = score
            db.session.commit()

    return redirect(url_for('result', score=score))


@app.route('/result')
def result():
    score = request.args.get('score')
    user = User.query.get(session['user_id'])
    highest_score = user.highest_score
    return render_template('result.html', score=score, highest_score=highest_score)


@app.context_processor
def inject_user():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return {'user': user}
    return {}


if __name__ == '__main__':
    app.run(debug=True)
