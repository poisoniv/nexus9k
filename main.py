from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/meraki")
def meraki():
    return render_template("meraki.html")

@app.route("/n9k")
def n9k():
    return render_template("nexus9k.html")

#@app.route("/functions")
#def functions():
#    return  "some json here"

if __name__ == "__main__":
    app.run(debug=True)