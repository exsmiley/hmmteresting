import requests

url = "http://127.0.0.1:5000/climate"

payload = {
    "room_size": "large",
    "people_30_ago": 2,
    "people_15_ago": 5,
    "people_now": 20,
    "people_next_30": 20,
    "people_next_1": 10,
    "weather_2_ago": 30,
    "weather_now": 30,
    "weather_next_1": 29,
    "room_temp_30_ago": 23,
    "room_temp_now": 23,
}

response = requests.request("POST", url, data=payload)
print(response.text)