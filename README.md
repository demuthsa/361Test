# Weather Advisory Microservice

## Introduction
This repository contains a Python-based weather application and its accompanying microservice. The main application fetches weather data and then interacts with the microservice to generate relevant weather advisories based on current conditions.

## Communication Contract
Our communication contract remains consistent to ensure reliability and clarity for all users and contributors. The main application sends weather data to the microservice, which then returns a weather advisory.

## Requesting Data

1. User Input Handling: In your main weather app file (main.py), the user provides input through the command line. This input specifies the location and optionally the units (imperial, metric, or standard) and whether additional information like wind speed, humidity, and pressure is desired.

2. API Call to Fetch Weather Data: The app makes an external API call to OpenWeatherMap using the provided location and units. It receives weather data in response, including temperature, weather description, etc.

3. Preparing Data for Microservice: The weather data, specifically temperature, description, and unit_symbol, is formatted into a JSON string. This is the data that will be sent to the microservice for further processing.

4. Calling the Microservice: The main app then calls the microservice (weatherAdvisoryMicroservice.py) using Python's subprocess module, passing the JSON string as an argument.

### Format
The microservice accepts JSON-formatted data containing the following fields:
- `temperature`: The current temperature (numeric).
- `description`: A brief description of the current weather (string).
- `unit_symbol`: The unit of the temperature, either "°F" or "°C" (string).

### Example Call
```
import subprocess
import json

input_data = json.dumps({
    "temperature": 72,
    "description": "clear sky",
    "unit_symbol": "°F"
})

output = subprocess.check_output(["python3", "weatherAdvisoryMicroservice.py", input_data])
print(output.decode())
```

## Receiving Data
This output is based on the weather conditions provided in the request.

1. Subprocess Call: In the main application, Python's subprocess module is used to call the microservice. This is done using subprocess.check_output(), which not only runs the microservice script but also captures its output. Here's the key part of your code that does this:
```
output = subprocess.check_output(["python3", "weatherAdvisoryMicroservice.py", input_data])
```
In this line, input_data is a JSON string sent to the microservice, and subprocess.check_output() is responsible for executing the microservice and capturing its output.

2. Microservice Processing: The microservice, upon execution, receives the JSON string, processes it to generate a weather advisory based on the provided data, and then prints the advisory.

3. Capturing Output: The output of the microservice (the printed weather advisory) is captured by the subprocess.check_output() method in the main application.

4. Decoding the Output: The captured output is in bytes, so you decode it to convert it into a string format which is more readable and usable:

```
print(output.decode())
```

5. Displaying the Advisory: Finally, the decoded string, which contains the weather advisory, is printed to the console, making it visible to the user.

## UML Sequence Diagram
Below is a UML sequence diagram illustrating the interaction between the main application and the microservice:


# Setup and Requirements

## Prerequisites
Python 3.x
Required Python libraries: requests, pyfiglet, simple_chalk

## Installation
Clone the repository and install the required dependencies:

```
git clone [repository-url]
cd [repository-name]
pip install -r requirements.txt
```

## Usage and Examples
Run the main application using the following command:
```
python3 main.py [city-name] or python3 main.py [city-name] --units [unit]
```
### For example:

python3 main.py London --units metric
