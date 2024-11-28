from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="MEOW")

@app.route('/text')
def text():
    textAp = "КРУТОЙ ТЕКСТ КОТОРЫЦЙ ПЕРЕДАЛСЯ"
    return render_template('text.html', title="Mur1", textAp=textAp)

@app.route('/image')
def image():
    return render_template('image.html', title="MEOW")

@app.route('/table')
def table():
    return render_template('table.html', title="MEOW")

@app.route('/listin')
def listin():
    songs = ["BLAMMED - Kawai Sprite", "фотографирую закат - fem.love", "Pico - Kawai Sprite"]
    return render_template('listin.html', songs=songs, title="MEOW")

@app.route('/auth', methods=['POST','GET'])
def auth():
    if request.method == 'POST':
        username = request.form['username']
        print("you cool")
        return render_template('authEnd.html', username=username, title="MEOW")
    else:
        return render_template('auth.html', title="MEOW")

if __name__ == '__main__':
    app.run(debug=True)