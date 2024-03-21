from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from form_register import *
from model import *

app = Flask(__name__)
app.config['SECRET_KEY'] = b'fd7d71c239fb32c72'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///a1.db'
db.init_app(app)


# #Генерация надёжного секретного ключа
# import secrets
# secrets.token_hex()


@app.route('/', methods=['GET', 'POST'])
@app.route('/reg/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user =UserHW3(firstname = form.firstname.data, lastname = form.lastname.data, email = form.email.data,
        password = form.password.data)
        print("ок")
        db.session.add(user)
        db.session.commit()
        return render_template('result.html', message='Регистрация завершена. Поздравляю!')
    return render_template('reg.html', form=form)

@app.cli.command('init-reg')
def init_db():
    db.create_all()
    print('OK')


@app.route('/data/')
def data():
    return 'data'


if __name__ == '__main__':
    app.run(debug=True)
