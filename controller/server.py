
from flask import Flask
from control_model import finished_model

app = Flask(__name__)

model = finished_model()

@app.route("/", methods=['GET'])
def ping():
    return 200

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
