from flask import Flask
from models import db
from flask import Flask, render_template
from flask import request
from flask import jsonify
app = Flask(__name__)
app.config['DEBUG'] = True

# index page
@app.route('/')
def index():
    return render_template('index.html')

# register
@app.route('/', methods=["POST"])
def register():
    # request from form
    data = {
        "name":request.form.get('name'),
        "email":request.form.get('email'),
        "phone":request.form.get('phone'),
        "birthday":request.form.get('birthday')
    }
    # become json format
    data = jsonify(data)
    return data

if __name__ == '__main__':
    app.run()