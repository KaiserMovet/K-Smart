from flask import Flask
print("fff")
app = Flask(__name__)



@app.route('/')
def hello_world():
    return "Aaaa"