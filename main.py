from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "we did it!"

@app.route("/autocomp")
def autocomp():
    return  "some json here"

app.run(debug=True)