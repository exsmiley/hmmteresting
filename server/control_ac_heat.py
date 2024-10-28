def control_ac_heat(people_30_ago, people_15_ago, people_now, people_next_30, people_next_1,
                    weather_2_ago, weather_now, weather_next_1, room_temp_30_ago, room_temp_now, room_size):
    # 최적 실내 온도 범위 설정
    optimal_temp_range = (22, 25)  # 22°C ~ 25°C
    
    # 사람 수 변화 추이 반영
    people_trend = (people_now - people_15_ago) + (people_15_ago - people_30_ago)
    future_people_trend = (people_next_1 - people_now) + (people_next_30 - people_now)
    
    # 외부 기온의 평균 및 예측 반영
    avg_weather = (weather_2_ago + weather_now + weather_next_1) / 3
    
    # 실내 크기 반영
    if room_size == "large":
        room_factor = 1.2  # 큰 방은 온도 변화가 느리므로 더 강한 조정이 필요함
    elif room_size == "medium":
        room_factor = 1.0  # 중간 크기는 기본값
    else:  # small
        room_factor = 0.8  # 작은 방은 온도 변화가 빠르므로 약한 조정이 필요함
    
    # 인원 수와 외부 기온, 방 크기를 기반으로 목표 온도 계산
    if avg_weather > 30:
        # 외부 기온이 높으면 에어컨이 더 필요할 수 있음
        target_temperature = room_temp_now - (people_now * 0.15 * room_factor) - (future_people_trend * 0.1)
    elif avg_weather < 15:
        # 외부 기온이 낮으면 히터가 필요할 수 있음
        target_temperature = room_temp_now + (people_now * 0.15 * room_factor) + (future_people_trend * 0.1)
    else:
        # 외부 기온이 쾌적할 경우, 현재 온도를 유지
        target_temperature = room_temp_now + (people_trend * 0.05 * room_factor)
    
    # 목표 온도를 최적 범위로 조정
    if target_temperature < optimal_temp_range[0]:
        target_temperature = optimal_temp_range[0]
    elif target_temperature > optimal_temp_range[1]:
        target_temperature = optimal_temp_range[1]
    
    # 에어컨과 히터의 작동 여부 결정
    if target_temperature > room_temp_now:
        ac_on = "no"  # 실내 온도가 낮으므로 히터를 켜야 함
        heat_on = "yes" if avg_weather < 30 else "no"  # 외부 기온이 30도 이하일 경우에만 히터를 켜기
    elif target_temperature < room_temp_now:
        ac_on = "yes"  # 실내 온도가 높으므로 에어컨을 켜야 함
        heat_on = "no"
    else:
        ac_on = "no"
        heat_on = "no"  # 실내 온도가 목표에 맞춰져 있으므로 아무 것도 켜지 않음
    
    return ac_on, heat_on
