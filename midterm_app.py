from flask import Flask, redirect, url_for, render_template, request

midtermapp = Flask(__name__)


@midtermapp.route("/", methods=['GET'])
def index():
    return render_template('login.html')


@midtermapp.route("/registration", methods=['GET', 'POST'])
def regis():
    return render_template('registration.html')


if __name__ == '__main__':
    midtermapp.run(debug=True, host='0.0.0.0', port=5000)
