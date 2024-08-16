from flask import Flask, request, jsonify, render_template,redirect, url_for

app = Flask(__name__)

@app.route('/',methods=["GET"])
def get_page():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)