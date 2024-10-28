import requests

url = "http://127.0.0.1/climate"

# payload = {
#     "room_size": "small",
#     "people_30_ago": 0,
#     "people_15_ago": 0,
#     "people_now": 1,
#     "people_next_30": 1,
#     "people_next_1": 0,
#     "weather_2_ago": 31,
#     "weather_now": 30,
#     "weather_next_1": 30,
#     "room_temp_30_ago": 26,
#     "room_temp_now": 27,
# }
payload = {
    "room_size": "large",
    "people_30_ago": 3,
    "people_15_ago": 10,
    "people_now": 15,
    "people_next_30": 10,
    "people_next_1": 10,
    "weather_2_ago": 26,
    "weather_now": 29,
    "weather_next_1": 31,
    "room_temp_30_ago": 24,
    "room_temp_now": 25,
}

response = requests.request("POST", url, data=payload)
print(response.text)