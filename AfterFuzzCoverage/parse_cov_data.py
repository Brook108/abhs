import csv
import json

# Read the file
with open('data.json', 'r') as f:
    data = json.load(f)

# Extract the relevant data
method_data = data['AllData'][1]['MethodCov']
parsed_data = []

for method in method_data:
    method_name = method['MethodName']
    class_name = method['ClassName']
    cdc = method['CDC']
    if cdc != '--':
        print("cdc:", cdc)
        cdc = round(float(cdc.rstrip('%')), 2)
        cdc = f"{cdc}%"

    cdc_runblock = method['cdcRunblock']
    cdc_sumblock = method['cdcSumblock']

    parsed_data.append([class_name, method_name,  cdc_runblock, cdc_sumblock, cdc])

# Write the data to a CSV file
with open('parsed_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['类名', '函数名', '覆盖分支数', '总分支数', '覆盖率'])  # Write header
    writer.writerows(parsed_data)

print("CSV file created successfully.")

