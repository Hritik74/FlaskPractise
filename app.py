## creating simple flask application
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Hritik Whats'up"

@app.route('/welcome')
def welcome():
    return "Welcome home Hritik. How are you Hritik?"


fruits = {
    'apple': {
        'description': 'A sweet, crispy fruit',
        'quantity': 10,
    },
    'banana': {
        'description': 'A tropical fruit with a yellow skin',
        'quantity': 5,
    },
    'orange': {
        'description': 'A citrus fruit with a juicy interior',
        'quantity': 7,
    },
    'grape': {
        'description': 'A small, sweet fruit often used to make raisins',
        'quantity': 15,
    },
}

@app.route('/index')
def index():
    total_fruits = sum(item['quantity'] for item in fruits.values())
    return render_template('index.html', fruits=fruits, total_fruits=total_fruits)




if __name__=='__main__':
    app.run(debug=True)

