from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Hello_World():
    return "Hello,World!"

@app.route("/Products")
def Products():
    #return "This is my Product"
    return render_template('index.html')

app.run(debug=True)    

