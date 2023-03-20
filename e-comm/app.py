from classes import Dog, Cat, Person
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'it works'

@app.route('/home/<user_name>')
def home(user_name):
    return render_template('home/home.html', title_user_name=user_name)

@app.route('/home/<user_name>/adoption')
def adoption(user_name):
    return render_template('adoption/adoption.html', title_user_name=user_name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login/login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup/signup.html')

@app.route('/signout')
def signout():
    return render_template('signout/signout.html')


@app.route('/api/methods/create.pet/<xtype>/<name>/<int:age>')
def create_pet(xtype: str, name: str, age: int):
    if xtype == 'Cat':
        new_pet = Cat(name, age)
        return f'{new_pet}'
    if xtype == 'Dog':
        new_pet = Dog(name, age)
        return f'{new_pet}'
    return f'see api documentation in order to learn the methods.'


if __name__ == '__main__':
    app.run(debug=True, port=8080)