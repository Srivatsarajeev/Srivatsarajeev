from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(_name_)

# Initialize the database
def init_db():
    with sqlite3.connect('feedback.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS feedback
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name TEXT NOT NULL,
                         email TEXT NOT NULL,
                         message TEXT NOT NULL)''')

@app.route('/')
def home():
    return redirect(url_for('feedback'))

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        with sqlite3.connect('feedback.db') as conn:
            conn.execute('INSERT INTO feedback (name, email, message) VALUES (?, ?, ?)', (name, email, message))
            conn.commit()
        return 'Thank you for your feedback!'
    return render_template('feedback.html')

if _name_ == '_main_':
    init_db()
    app.run(debug=True)