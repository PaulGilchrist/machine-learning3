import subprocess
import json
# Define input data
input_data = {
    "param1": "value1",
    "param2": "value2"
}
# Serialize input data to JSON
input_json = json.dumps(input_data)
# Call NodeJS module and pass input data as argument
node_output = subprocess.check_output(["node", "module.js", input_json])
# Deserialize output data from JSON
output_data = json.loads(node_output)
# Print output data
print(output_data)
