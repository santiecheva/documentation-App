"""
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://santiago:cofifi73@localhost/documentationapp'


users = [
    {
        "Username": "Admin",
        "Age": "25"
    },
    {
        "Username": "Santiago",
        "Age": "27"
    }
]


@app.route('/users', methods=["GET"])
def get_all_users():
    return jsonify(users)


@app.route('/users/<string:username>', methods=["GET"])
def get_user_by_name(username):
    result = next((user for user in users if user["Username"] == username), None)
    if result is not None:
        return jsonify(result), 200
    else:
        return "User not found", 404


if __name__ == '__main__':
    app.run(debug=True)
"""