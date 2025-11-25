# import flask modules
from flask import Flask, jsonify, render_template

## create the flask instance
app = Flask(__name__)

#  define function and route
# '/', "/about us", "/data"


# @app.route("/")
# def home():
#     return "Welcome to the Home Page!"


@app.route("/about us")
def about():
    return """<h1>About Us</h1><br>
             <h2>Our Company</h2><br>
             <p>We are not dedicated to providing the best services to our customers.</p>"""


@app.route("/data")
def data():
    user_data = {"name": "John Doe", "Age": 30, "city": "New York"}
    return jsonify(user_data)


# @app.route("/")
# def html_page():
#     Name = "John"
#     return render_template("index.html", name=Name)


# @app.route("/", methods=["GET"])
# def html_page():
#     # Name = "John"
#     return "Hello World!"


@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def welcome():
    return "Hello, we have received your submission!"


## trigger the flask app
if __name__ == "__main__":
    app.run(debug=True)
