from flask import Flask, request, jsonify, render_template,redirect, url_for

app = Flask(__name__)

# Route: Home
@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")

# Route: Masterworks
@app.route('/masterworks', methods=["GET"])
def masterworks():
    return render_template("error.html")

# Route: About Us
@app.route('/about', methods=["GET"])
def about_us():
    return render_template("error.html")

# Route: Submissions
@app.route('/submissions', methods=["GET"])
def submissions():
    return render_template("error.html")

# Route: Editions
@app.route('/editions', methods=["GET"])
def editions():
    return render_template("error.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)