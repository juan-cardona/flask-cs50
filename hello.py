from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello how , {name}</h1>"
    