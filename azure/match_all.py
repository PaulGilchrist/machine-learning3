# This module allows for local development and debugging of the Azure Machine Learning module named `azureMatch`
# Imports
import azure.azure_match as azure_match

#Configuration
input_file = "../inputs/materials.csv"
output_file = "../outputs/material_matches.csv"
azure_match.min_probability = None # Set to None if wanting to prompt user, otherwise, set between 0 and 100 with 100 representing an exact match
azure_match.logging_level = 3 # 0=Errors, 1=Errors and Warnings, 2=Errors, Warnings, and Informational, 3=Errors, Warnings, Informational, and Debug

# Read CSV data file
input_dataframe1 = azure_match.pd.read_csv(input_file)
# Log Input Summary
materials_count = len(input_dataframe1.index)
comparisons_needed = int((materials_count*(materials_count-1))/2)
azure_match.log(2, "\n{:,} Materials found".format(materials_count))
azure_match.log(2, "{:,} Comparisons needed".format(comparisons_needed))
if(azure_match.min_probability == None):
    azure_match.min_probability = int(input("\nSet minimum probability between 0 and 100: ")) 
azure_match.log(2, "\nProcessing...\n")
# Call same function we would use for Azure Machine Learning
output_dataframe1 = azure_match.azureml_main(input_dataframe1)
output_dataframe1.to_csv(output_file)
# Log Output Summary
possible_matches_found = len(output_dataframe1.index)
azure_match.log(2, "\n{:,} Possible matches found\n".format(possible_matches_found))
