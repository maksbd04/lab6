from flask import Flask, request, jsonify, render_template
import json


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("hom.html")


@app.route("/students_list")
def students_list():
    e = json.load(open('base/students_list.json'))
    eee = e['students']
    return render_template('students_list.html', students=eee)


if __name__ == "__main__":
    app.run()