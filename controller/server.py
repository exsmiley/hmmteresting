from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import traceback
from control_model import finished_model 
from data import datadict_to_vectors

app = Flask(__name__)
# CORS 설정을 더 구체적으로 지정
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

model = finished_model()

@app.route("/", methods=['GET'])
def ping():
    return "OK"

@app.route("/climate", methods=['POST', 'OPTIONS'])  # OPTIONS 메소드 추가
def climate_api():
    # OPTIONS 요청 처리
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        return response

    try:
        vec, _ = datadict_to_vectors(request.form)
        vec = torch.as_tensor(vec)
        outputs = model(vec)
        response = vec_output_to_output(outputs)
        # CORS 헤더 추가
        return response
    except Exception as e:
        error_msg = {
            "error": str(e),
            "traceback": traceback.format_exc()
        }
        return jsonify(error_msg), 500


def vec_output_to_output(outputs):
    try:
        ac_on = 0
        heat_on = 0
        if outputs[1] > 0.5:
            ac_on = 1
        if outputs[2] > 0.5:
            heat_on = 1


        temp = outputs[0] * 40 - 5
        return jsonify({
            "ac": ac_on,
            "ac_conf": outputs[1].tolist(),
            "heat": heat_on,
            "heat_conf": outputs[2].tolist(),
            "temperature": temp.tolist(),
            "temperature_val": outputs[0].tolist(),
        })
    except Exception as e:
        error_msg = {
            "error": str(e),
            "traceback": traceback.format_exc()
        }
        return jsonify(error_msg), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
