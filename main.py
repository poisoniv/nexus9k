from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "we fucking did it!"

@app.route("/autocomp")
def autocomp():
    return  "some fuckiong json here"

app.run(debug=True)