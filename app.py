from flask import Flask, render_template, jsonify, request
import requests
import os
import json
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/_led1")
def _led1():
    state_led1 = request.args.get("state_led1")
    s = {"led_1": state_led1}

    fname = os.path.join(app.static_folder, "led_1.json")
    with open(fname, "w") as outfile:
        json.dump(s, outfile)

    return "success"

@app.route("/_led2")
def _led2():
    state_led2 = request.args.get("state_led2")
    s = {"led_2": state_led2}

    fname = os.path.join(app.static_folder, "led_2.json")
    with open(fname, "w") as outfile:
        json.dump(s, outfile)

    return "success"

@app.route("/_led3")
def _led3():
    state_led3 = request.args.get("state_led3")
    s = {"led_3": state_led3}
    fname = os.path.join(app.static_folder, "led_3.json")
    with open(fname, "w") as outfile:
        json.dump(s, outfile)

    return "success"


@app.route("/read_led1")
def readJSON_led1():
    fname = os.path.join(app.static_folder, "led_1.json")
    with open(fname, "r") as openfile:
        json_obj = json.load(openfile)
    return json_obj

@app.route("/read_led2")
def readJSON_led2():
    fname = os.path.join(app.static_folder, "led_2.json")
    with open(fname, "r") as openfile:
        json_obj = json.load(openfile)
    return json_obj

@app.route("/read_led3")
def readJSON_led3():
    fname = os.path.join(app.static_folder, "led_3.json")
    with open(fname, "r") as openfile:
        json_obj = json.load(openfile)
    return json_obj


if __name__ == "__main__":
    app.run(debug=True)
