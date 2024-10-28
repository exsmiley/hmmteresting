import csv

def load_data():
    data = []
    csv_file = 'training_data.csv'
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['people_30_ago'] == '':
                continue
            vec, labels = datadict_to_vectors(row)
            data.append((vec, labels))
    return data


def datadict_to_vectors(row):
    vec = []
    
    if 'room_size' in row:
        if row['room_size'] == "small":
            vec.append(1)
            vec.append(0)
            vec.append(0)
        elif row['room_size'] == 'medium':
            vec.append(0)
            vec.append(1)
            vec.append(0)
        else:
            vec.append(0)
            vec.append(0)
            vec.append(1)
    else:
        vec.append(0)
        vec.append(1)
        vec.append(0)

    vec.append(normalize_people(row['people_30_ago']))
    vec.append(normalize_people(row['people_15_ago']))
    vec.append(normalize_people(row['people_now']))
    vec.append(normalize_people(row['people_next_30']))
    vec.append(normalize_people(row['people_next_1']))

    vec.append(normalize_temperature(row['weather_2_ago']))
    vec.append(normalize_temperature(row['weather_now']))
    vec.append(normalize_temperature(row['weather_next_1']))
    vec.append(normalize_temperature(row['room_temp_30_ago']))
    vec.append(normalize_temperature(row['room_temp_now']))

    labels = [
        normalize_temperature(row.get('desired_temp', 0)),
        1 if row.get('ac_on', '') == 'yes' else 0,
        1 if row.get('heat_on', '') == 'yes' else 0
    ]

    return vec, labels


def normalize_people(people_count):
    people_count = int(people_count)
    zero_penalty = 20
    upper_bound = 25
    if people_count < 0:
        people_count = -zero_penalty
    if people_count > upper_bound:
        people_count = upper_bound
    return (people_count + zero_penalty) / (upper_bound + zero_penalty)


def normalize_temperature(temp):
    temp = int(temp)
    if temp < -5:
        temp = -5
    if temp > 35:
        temp = 35

    return (temp + 5)/ 40

if __name__ == "__main__":
    a = load_data()

    for i, (vec, labels) in enumerate(a):
        print("v", vec)
        print("l", labels)