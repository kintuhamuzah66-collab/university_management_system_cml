import json

data = {
    'erinnya': "Kintu Hamza",
    'Eddaala': "University",
    "Ow'omukwano": "Saidah",
}

data_json = json.dumps(data)
print(data_json, type(data_json))

deserialized_json = json.loads(data_json)
print(deserialized_json, type(deserialized_json))