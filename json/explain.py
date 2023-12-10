"""
need to import json
    Import json

Open json file 
    f = open('data.json') 
        # "data.json" - name of the file 
        # "f" is the file itself 

Return Json object as a dictionary
    data = json.load(f)
        # data is now the full content of 'data.json' (file)
"""

# ====================================================================================


"""
Video class

json = Java script object notation

Use "" not ''

"""

# ====================================================================================


"""
Certainly! Here's a comprehensive summary of working with JSON in Python:

### JSON (JavaScript Object Notation):

**Definition:**
- JSON is a lightweight data interchange format that is easy for humans to read and write. It is also easy for machines to parse and generate.

**Python JSON Module (`json`):**
- The `json` module in Python provides methods for encoding and decoding JSON data.
- It is part of the Python standard library, so no additional installation is required.

#### JSON Encoding (Python to JSON):

1. **`json.dumps(obj, indent=None, separators=None, default=None, ...)`:**
   - Converts a Python object (`obj`) to a JSON-formatted string.
   - `indent`: Controls the indentation of the JSON string.
   - `separators`: Specifies custom separators for the JSON string.
   - `default`: A function to convert non-JSON serializable objects.

2. **`json.dump(obj, fp, indent=None, separators=None, default=None, ...)`:**
   - Writes a Python object (`obj`) to a file-like object (`fp`) in JSON format.
   - Similar parameters to `json.dumps`.

#### JSON Decoding (JSON to Python):

1. **`json.loads(s, ..., parse_float=None, parse_int=None, ...)`:**
   - Parses a JSON-formatted string (`s`) and returns a Python object.
   - `parse_float`: A function to convert JSON floats.
   - `parse_int`: A function to convert JSON integers.

2. **`json.load(fp, ..., parse_float=None, parse_int=None, ...)`:**
   - Reads a JSON-formatted file-like object (`fp`) and returns a Python object.
   - Similar parameters to `json.loads`.

#### Example:

```python
import json

# Python object to JSON string
python_object = {'key': 'value', 'numbers': [1, 2, 3]}
json_string = json.dumps(python_object, indent=2)

# JSON string to Python object
decoded_object = json.loads(json_string)

# Writing Python object to JSON file
with open('example.json', 'w') as json_file:
    json.dump(python_object, json_file, indent=2)

# Reading JSON file to Python object
with open('example.json', 'r') as json_file:
    loaded_object = json.load(json_file)
```

**Note:**
- JSON supports basic data types: objects, arrays, strings, numbers, booleans, and `null`.
- Python objects like dictionaries, lists, strings, integers, floats, and `None` can be easily converted to and from JSON.
- It's important to handle exceptions (`json.JSONDecodeError`, `json.JSONEncodeError`) when working with JSON to handle potential errors in the data.

JSON is commonly used for data exchange between different systems and languages due to its simplicity and readability. The Python `json` module provides a convenient and effective way to work with JSON data in Python applications.
"""

# ====================================================================================


"""
In Python, the modes "r," "w," "r+", and "a" are used when opening a file, including JSON files. These modes determine the type of access you have to the file and whether the file is created if it doesn't exist. These modes are commonly used with functions like `open` and `json.dump`/`json.load`.

1. **"r" (Read):**
   - Opens the file for reading only.
   - Raises an error if the file does not exist.
   - The file pointer is placed at the beginning of the file.

   ```python
   with open('example.json', 'r') as file:
       content = file.read()
   ```

2. **"w" (Write):**
   - Opens the file for writing only.
   - Truncates the file to zero length or creates the file if it doesn't exist.
   - The file pointer is placed at the beginning of the file.

   ```python
   with open('example.json', 'w') as file:
       file.write('{"key": "value"}')
   ```

3. **"r+" (Read and Write):**
   - Opens the file for both reading and writing.
   - Raises an error if the file does not exist.
   - The file pointer is placed at the beginning of the file.

   ```python
   with open('example.json', 'r+') as file:
       content = file.read()
       # Perform read and write operations
   ```

4. **"a" (Append):**
   - Opens the file for writing only.
   - Creates the file if it doesn't exist.
   - The file pointer is placed at the end of the file.
   - New data will be written at the end, preserving existing content.

   ```python
   with open('example.json', 'a') as file:
       file.write('{"key": "value"}')
   ```

When working specifically with JSON files, the "r" mode is commonly used for reading JSON data, and the "w" or "a" modes are used for writing JSON data. The "r+" mode can be used for both reading and writing, and it requires that the file already exists.

```python
import json

# Reading JSON from file
with open('example.json', 'r') as file:
    data = json.load(file)

# Writing JSON to file (overwrite existing content)
with open('example.json', 'w') as file:
    json.dump(data, file, indent=2)

# Appending JSON to file (preserving existing content)
with open('example.json', 'a') as file:
    json.dump({"new_key": "new_value"}, file, indent=2)
```

"""