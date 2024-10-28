from flask import Flask, jsonify, abort
from utils import (
    get_room_temperature,
    calculate_people_change,
    calculate_occupancy_change,
    find_max_occupancy_increase,
    find_most_populated_space,
    calculate_ac_temperature
)

app = Flask(__name__)

# 각 방의 임의 온도를 반환
# API Endpoint to get the temperature of a specific space
@app.route('/api/space/<space_name>/temperature', methods=['GET'])
def get_space_temperature(space_name):
    temperature = get_room_temperature(space_name)

    if temperature is None:
        abort(404, description="Invalid space or data not available")
    
    return jsonify({
        "space_name": space_name,
        "temperature": temperature,
        "status": "Success"
    }), 200


# 밀면이 API 필요
# 인원 증감 수 
# API Endpoint to calculate people change for a specific space
@app.route('/api/space/<space_name>/people_change/<int:current_count>', methods=['GET'])
def get_people_change(space_name, current_count):
    try:
        result = calculate_people_change(space_name, current_count)
        return jsonify(result), 200
    except Exception as e:
        abort(500, description=str(e))


# 특정 방의 1시간 동안의 이용률 변화를 계산
# API Endpoint to get occupancy change for a specific space
@app.route('/api/space/<space_name>/occupancy_change', methods=['GET'])
def get_occupancy_change(space_name):
    result = calculate_occupancy_change(space_name)
    
    if result is None:
        abort(404, description="Invalid space or data not available")

    return jsonify(result), 200


# 1시간 동안 이용률이 가장 많이 증가한 방을 찾아서 반환
# API Endpoint to find the space with the maximum occupancy increase in the last hour
@app.route('/api/occupancy/increase', methods=['GET'])
def get_max_occupancy_increase():
    result = find_max_occupancy_increase()
    
    if result is None:
        abort(404, description="No data available")

    return jsonify(result), 200


# 현재 가장 사람이 많은 공간을 찾아서 반환
# API Endpoint to find the most populated space currently
@app.route('/api/occupancy/most_populated', methods=['GET'])
def get_most_populated_space():
    result = find_most_populated_space()
    
    if result is None:
        abort(404, description="No data available")

    return jsonify(result), 200


# 에어컨 설정 온도를 계산
# API Endpoint to calculate AC temperature settings for a specific space
@app.route('/api/space/<space_name>/ac_temperature/<int:current_people_count>', methods=['GET'])
def get_ac_temperature(space_name, current_people_count):
    result = calculate_ac_temperature(space_name, current_people_count)
    
    if 'error' in result:
        abort(400, description=result['error'])

    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)
