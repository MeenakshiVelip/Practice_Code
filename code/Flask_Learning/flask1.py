from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello_World():
    return "Hello,World!"

@app.route("/Products")
def Products():
    return "This is my Product"

app.run(debug=True)    
