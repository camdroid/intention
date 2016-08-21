from flask import Flask
from flask import render_template
import pomodoro

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html', minutes_from_flask=15)

if __name__ == '__main__':
    pomo = pomodoro.Pomodoro(1)
    app.run()
