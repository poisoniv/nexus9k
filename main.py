from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "we did it!"

@app.route("/functions")
def functions():
    return  "some json here"

if __name__ == "__main__":
    app.run(debug=True)