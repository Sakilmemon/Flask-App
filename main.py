# import flask
from flask import Flask

## create the flask instance
app = Flask(__name__)

#  define function and route
# '/', "/about us", "/data"


@app.route("/")
def home():
    return "Welcome to the Home Page!"


@app.route("/about us")
def about():
    data = "This is the About Us Page."
    return data


@app.route("/data")
def data():
    user_data = "Here is some data."
    return user_data


## trigger the flask app
if __name__ == "__main__":
    app.run(debug=True)
