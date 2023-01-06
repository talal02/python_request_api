from flask import Flask, request, jsonify, make_response
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/getApp', methods=['GET'])
def respond():
        currentMonth = str(datetime.now().month)
        currentYear = str(datetime.now().year)
        if len(currentMonth) == 1:
            currentMonth = '0' + currentMonth
        url = f"https://acuityscheduling.com/api/v1/availability/dates?month={currentYear}-{currentMonth}&appointmentTypeID=34129789"

        headers = {
        "Accept": "application/json",
        "Authorization": "Basic MjA4MDEyNjA6Y2QzNjA2NzUxYTI1ZTkzZDUyYzcwYzRlNWM4ZWM5MDE="
        }

        response = requests.get(url, headers=headers)
        
        if len(response.text) <= 2:
            return build_res(jsonify({"message": "No Appointments Available"}))

        date = response.text[10:20]


        url = f"https://acuityscheduling.com/api/v1/availability/times?date={date}&appointmentTypeID=34129789"

        response = requests.get(url, headers=headers)


        return build_res(jsonify(response.json()))


def build_res(_res):
    _res.headers.add("Access-Control-Allow-Origin", "*")
    _res.headers.add('Access-Control-Allow-Headers', "*")
    _res.headers.add('Access-Control-Allow-Methods', "*")
    return _res


@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our medium-greeting-api!</h1>"
