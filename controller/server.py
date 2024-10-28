from flask import Flask, request
import torch
from control_model import finished_model
from data import datadict_to_vectors

app = Flask(__name__)

model = finished_model()

@app.route("/climate", methods=['POST'])
def climate_api():
    vec, _ = datadict_to_vectors(request.form)
    vec = torch.as_tensor(vec)
    outputs = model(vec)
    # return {
    #     "ac": False,
    #     "ac_conf": 0.1,
    #     "heat": False,
    #     "heat_conf": 0.1,
    #     "temperature": 23,
    #     "temperature_val": 0.8,
    # }
    return vec_output_to_output(outputs)


def vec_output_to_output(outputs):
    ac_on = 0
    heat_on = 0
    if outputs[1] > 0.5:
        ac_on = 1
    if outputs[2] > 0.5:
        heat_on = 1

    return {
        "ac": ac_on,
        "ac_conf": outputs[1].tolist(),
        "heat": heat_on,
        "heat_conf": outputs[2].tolist(),
        "temperature": 23,
        "temperature_val": outputs[0].tolist(),
    }
