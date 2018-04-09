from flask import Flask
# from models import db
from flask import Flask, render_template
from flask import request
from flask import jsonify
from data_process import PostgreDbProcess
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
        "table":"users",
        "columns": "id, name, email, birthday, register_time",
        "name":request.form.get('name'),
        "email":request.form.get('email'),
        "phone":request.form.get('phone'),
        "birthday":request.form.get('birthday'),
        "table": "users",
        "register_time":"2018-10-11"
    }
    # become json format
    # post_data = jsonify(data)
    insert_data = PostgreDbProcess(data)
    insert_data.insert()
    return 'insert ok!'

if __name__ == '__main__':
    app.run()