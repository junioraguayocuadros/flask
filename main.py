import unittest

from flask import request, make_response, redirect, render_template, session

from app import create_app
from app.firestore_service import get_users

app = create_app()

todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar video del producto']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET'])
def hello():
    user_ip = session.get('user_ip')

    username = session.get('username')
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'username': username,
    }

    users = get_users()
    for user in users:
        print(user.id)
        print(user.to_dict()['password'])

    return render_template('hello.html', **context)
