import json

# Specify the path to your JSON file
json_file_path = 'json/char_classes.json'

# Read the content of the JSON file
with open(json_file_path, 'r') as file:
    json_content = file.read()

# Parse the JSON content using json.loads
parsed_json = json.loads(json_content)

# Now, `parsed_json` is a Python dictionary containing the data from the JSON file
print(parsed_json)
