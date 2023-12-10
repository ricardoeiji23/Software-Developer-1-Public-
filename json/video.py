import json

myDictionary = {
    "people": [
        {
            "name": "bob",
            "age": 22,
            "weight": 80,
        }
        {
            "name": "Anna",
            "age": 34,
            "weight": 67,
        }
        {
            "name": "Charles",
            "age": 45,
            "weight": 78,
        }
        {
            "name": "Daniel",
            "age": 21,
            "weight": 110,
        }
    ]
}

json_string = json.dumps(myDictionary)
    # .dumps() - Turn the json object and turns it into a string
    # Now we get the json string

with open('char_class.json', 'w') as f:
    f.write(json_string)
