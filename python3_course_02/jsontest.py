import json
import os

data = [
    {
        'user_id': 1000,
        'name': 'Shiyan',
        'pass': 10,
        'study_time': 50,
    },
    {
        'user_id': 2000,
        'name': 'Lou',
        'pass': 15,
        'study_time': 1
    }
]

file_name="tmp/jsontest.json"
file_path = os.path.dirname(file_name)
print(file_path)
if not os.path.exists(file_path):
    os.makedirs(file_path)
with open(file_name,'a') as file:
    file.write(json.dumps(data))