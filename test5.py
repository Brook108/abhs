import json

# Open the JSON file
file_path = "AMUST覆盖数据20230613.json"
with open(file_path) as file:
    # Load the JSON data
    data = json.load(file)

# Access the relevant data from the parsed JSON
all_data = data['AllData'][1]
method_cov = all_data['MethodCov']

# Initialize branches_num_map as an empty dictionary
branches_num_map = {}

# Iterate over the method coverage data
for method in method_cov:
    class_name = method['ClassName']
    method_name = method['MethodName']
    coverage = method['Branch']
    branches_num = method['cdcSumblock']

    # Create the key as class_name + ":" + method_name + ":" + coverage
    key = class_name + ":" + method_name + ":" + coverage

    # Assign branches_num to the corresponding key in the branches_num_map
    branches_num_map[key] = branches_num

# Print the resulting map
for key, value in branches_num_map.items():
    print(key, "->", value)
