from flask import Flask, render_template, request, redirect, url_for, flash, session
from .models import db, Auth, User, Education, Skills, Type_skills, Socials, Type_socials

app = Flask(__name__)

@app.route('/')
@app.route('/base')
def base():
    username = "LOGIN/REGISTER"
    
        
    return render_template('base.html', username=username, title="MEOW")

@app.route('/auth', methods=['POST','GET'])
def auth():
    if request.method == 'POST':
        username = request.form['username']
        print("you cool")
        return render_template('register.html', username=username, title="MEOW")
    else:
        return render_template('login.html', title="MEOW")

if __name__ == '__main__':
    app.run(debug=True)