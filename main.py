from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

### This is the part I'm not sure about...
#@app.route("/meraki")
#def index():
#    return render_template("index.html")

#@app.route("/functions")
#def functions():
#    return  "some json here"

if __name__ == "__main__":
    app.run(debug=True)