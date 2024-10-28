import random
import datetime


# 공간별 이전 인원 수
previous_people_count = {
    'shared_kitchen': 0,
    'launderette': 0,
    'meeting_room' : 0,
    'gym': 0,
    'multi-function_room' : 0,
    'lobby': 0
}

# 각 방의 최근 2시간 동안의 가상 이용률 데이터를 시간 단위로 저장
occupancy_data = {
    'shared_kitchen': [(datetime.datetime.now() - datetime.timedelta(hours=1), 5),  # 1시간 전, 5명
                    (datetime.datetime.now(), 12)],  # 현재, 12명
    'launderette': [(datetime.datetime.now() - datetime.timedelta(hours=1), 3),
                    (datetime.datetime.now(), 7)],  # 1시간 전, 3명 -> 현재, 7명
    'meeting_room': [(datetime.datetime.now() - datetime.timedelta(hours=1), 2),
                    (datetime.datetime.now(), 5)],  # 1시간 전, 2명 -> 현재, 5명
    'gym': [(datetime.datetime.now() - datetime.timedelta(hours=1), 10),
            (datetime.datetime.now(), 15)],  # 1시간 전, 10명 -> 현재, 15명
    'multi-function_room': [(datetime.datetime.now() - datetime.timedelta(hours=1), 6),
                            (datetime.datetime.now(), 8)],  # 1시간 전, 6명 -> 현재, 8명
    'lounge': [(datetime.datetime.now() - datetime.timedelta(hours=1), 8),
                (datetime.datetime.now(), 10)]  # 1시간 전, 8명 -> 현재, 10명
}


# 밀면이 API 필요
# 인원 증감 수
def calculate_people_change(space_name, current_count):
    # 이전 인원 수 가져오기
    previous_count = previous_people_count.get(space_name, 0)
    people_change = current_count - previous_count

    # 이전 인원 수 업데이트
    previous_people_count[space_name] = current_count

    # 상태 메시지 작성
    if people_change > 0:
        status = f"Increase of {people_change} people"
    elif people_change < 0:
        status = f"Decrease of {-people_change} people"
    else:
        status = "No change in number of people"

    return {
        "space_name": space_name,
        "current_people_count": current_count,
        "people_change": people_change,
        "status": status
    }


# 특정 방의 1시간 동안의 이용률 변화를 계산
def calculate_occupancy_change(space_name):
    if space_name not in occupancy_data:
        return None
    
    one_hour_ago, past_occupancy = occupancy_data[space_name][0]
    now, current_occupancy = occupancy_data[space_name][1]
    
    change_in_occupancy = current_occupancy - past_occupancy
    
    # 과거 인원 수가 0일 때 처리
    if past_occupancy == 0:
        if current_occupancy > 0:
            change_percentage = float('inf')  # 무한대 증가 (또는 임의의 큰 값으로 설정 가능)
        else:
            change_percentage = 0  # 과거와 현재 모두 0명인 경우 변화 없음
    else:
        change_percentage = (change_in_occupancy / past_occupancy) * 100
    
    return {
        "space_name": space_name,
        "past_occupancy": past_occupancy,
        "current_occupancy": current_occupancy,
        "change_in_occupancy": change_in_occupancy,
        "change_percentage": round(change_percentage, 2) if change_percentage != float('inf') else "Inf"  # 무한대는 별도 처리
    }



# 1시간 동안 이용률이 가장 많이 증가한 방을 찾아서 반환
def find_max_occupancy_increase():
    max_increase_room = None
    max_increase_percentage = -float('inf')

    for space_name in occupancy_data:
        occupancy_change = calculate_occupancy_change(space_name)
        if occupancy_change['change_percentage'] > max_increase_percentage:
            max_increase_room = occupancy_change
            max_increase_percentage = occupancy_change['change_percentage']
    
    return max_increase_room


# 현재 가장 사람이 많은 공간을 찾아서 반환
def find_most_populated_space():
    max_people_count = -1
    most_populated_space = None

    for space_name, occupancy in occupancy_data.items():
        _, current_people_count = occupancy[-1]  # occupancy 리스트의 마지막 항목에서 현재 인원 수를 가져옴
        
        if current_people_count > max_people_count:
            max_people_count = current_people_count
            most_populated_space = space_name

    return {
        "most_populated_space": most_populated_space,
        "current_people_count": max_people_count
    }


# 각 방의 임의 온도를 반환
# 실제 환경에서는 이 부분을 실제 Thermostat 장치 API로 교체
def get_room_temperature(space_name):
    temperature_data = {
        # 21~24도내에서 랜덤하게 생성하고, 소수점 둘째 자리까지 반올림
        'shared_kitchen': round(random.uniform(21, 24), 2),  # 공용 주방
        'gym': round(random.uniform(19, 23), 2),            # 체육관
        'event_hall': round(random.uniform(20, 25), 2),     # 이벤트 홀
        'multipurpose_room': round(random.uniform(22, 26), 2), # 다용도실
        'study_room': round(random.uniform(20, 24), 2)      # 스터디 룸
    }

    return temperature_data.get(space_name, None)


# Mock 외부 날씨 API 호출 (날씨 API로부터 받아오는 데이터로 교체)
def get_outdoor_temperature():
    # 외부 날씨 기온을 임의로 25°C에서 35°C 사이로 생성
    return round(random.uniform(25, 35), 2)


# 밀면이 API 필요
# 에어컨 설정 온도를 계산
def calculate_ac_temperature(space_name, current_people_count):
    # 현재 방의 온도
    current_room_temperature = get_room_temperature(space_name)
    
    if current_room_temperature is None:
        return {"error": f"Room '{space_name}' does not exist."}
    
    # 외부 날씨 온도
    outdoor_temperature = get_outdoor_temperature()
    
    # 기본 목표 실내 온도 범위 설정 (22~25°C)
    optimal_temperature_range = (22, 25)
    
    # 기본 목표 온도를 현재 방 온도로 설정
    target_temperature = current_room_temperature
    
    # 인원 수가 많으면 실내 온도를 낮춤 (인원 10명 이상일 경우 1°C 낮춤)
    if current_people_count > 10:
        target_temperature -= 1
    
    # 외부 기온이 30°C 이상이면 실내 온도를 더 낮춰야 함
    if outdoor_temperature >= 30:
        target_temperature -= 1
    
    # 목표 온도가 적정 범위 (22~25°C) 이내로 맞춰지도록 조정
    if target_temperature < optimal_temperature_range[0]:
        target_temperature = optimal_temperature_range[0]
    elif target_temperature > optimal_temperature_range[1]:
        target_temperature = optimal_temperature_range[1]
    
    # 에어컨을 올려야 하는지, 내려야 하는지, 유지해야 하는지를 결정
    if target_temperature > current_room_temperature:
        ac_action = "increase"
    elif target_temperature < current_room_temperature:
        ac_action = "decrease"
    else:
        ac_action = "maintain"
    
    return {
        "space_name": space_name,
        "current_people_count": current_people_count,
        "current_room_temperature": current_room_temperature,
        "outdoor_temperature": outdoor_temperature,
        "target_ac_temperature": target_temperature,
        "ac_action": ac_action
    }
