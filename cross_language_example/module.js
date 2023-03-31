// Read input data from command-line arguments
const inputJson = process.argv[2];
// Parse input data from JSON
const inputData = JSON.parse(inputJson);
// Process input data and generate output data
const outputData = {
    "result1": inputData.param1.toUpperCase(),
    "result2": inputData.param2.toLowerCase()
};
// Serialize output data to JSON and write to standard output
const outputJson = JSON.stringify(outputData);
console.log(outputJson);
