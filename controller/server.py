from flask import Flask
from control_model import finished_model

app = Flask(__name__)

model = finished_model()

@app.route("/climate", methods=['POST'])
def climate_api():
    # TODO get form data from request
    return {
        "ac": False,
        "ac_conf": 0.1,
        "heat": False,
        "heat_conf": 0.1,
        "temperature": 23,
        "temperature_val": 0.8,
    }
