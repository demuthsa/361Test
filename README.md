# Weather Advisory Microservice

## Introduction
This repository contains a Python-based weather application and its accompanying microservice. The main application fetches weather data and then interacts with the microservice to generate relevant weather advisories based on current conditions.

## Communication Contract
Our communication contract remains consistent to ensure reliability and clarity for all users and contributors. The main application sends weather data to the microservice, which then returns a weather advisory.

## Requesting Data

1. User Input Processing: The main app starts by processing user input. This is done using the argparse library, where you parse command-line arguments to get the desired location and optionally, the units for temperature, and whether additional weather information is desired.

2. Fetching Weather Data from External API: With the user's input, the app makes an API call to OpenWeatherMap to get real-time weather data for the specified location. This data includes temperature, weather conditions, etc.

3. Formatting Data for Microservice: After fetching the weather data, extract and format the necessary pieces of information (temperature, weather description, and unit of temperature) into a JSON string. This JSON string is what will be sent to the microservice. The code snippet for this would be:

```
input_data = json.dumps({
    "temperature": temperature,
    "description": description,
    "unit_symbol": unit_symbol
})
```

4. Calling the Microservice with Data: The next step is to call the microservice and pass it the formatted data. This is done using Python's subprocess module. The subprocess.check_output() function is used to call the microservice script (weatherAdvisoryMicroservice.py) and pass the JSON string as an argument:
```
output = subprocess.check_output(["python3", "weatherAdvisoryMicroservice.py", input_data])
```
In this command, weatherAdvisoryMicroservice.py is the script we are calling, and input_data is the argument being passed to it.

5. Microservice Processes Request: Upon execution, the microservice receives this JSON string as input. It then processes this data - extracting the temperature, weather description, and temperature unit to generate a weather advisory.



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
