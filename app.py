import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return f"Enter a number and I will add 10 to it and return the sum!"


@app.route('/<num>')
def get_num(num):
    num = int(num) + int(10)
    return flask.jsonify(sum=num)


if __name__ == '__main__':
    app.run()
