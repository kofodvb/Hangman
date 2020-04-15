import random
from flask import Flask, render_template, session, redirect, url_for, request
from markupsafe import escape
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F5G8z\n\xec]/'



@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        session['turns'] = request.form['turns']
        return redirect(url_for('index'))
    return

        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>





@app.route('/')
def show_user():
    return render_template('show_user.html')

@app.route('/new_game')
def start_new_game():
    if 'word' in session:
        return 'Dit ord er fundet'


    return render_template('new_game.html')

@app.route('/guess_word')
def guess_word():
    words = ['regnbue','vandmand','isbil']
    word = random.choice(words)
    turns = 7
    char = request.form

@app.route('/give_up')
def give_up():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))





if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
