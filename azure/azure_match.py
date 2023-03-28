# The Azure Machine Learning scripts MUST contain a function named azureml_main which is the entry point for Azure Machine Learning
import importlib.util
import os
if importlib.util.find_spec("thefuzz") is None:
    os.system(f"%pip install thefuzz") # Not a standard library of Azure Machine Learning
if importlib.util.find_spec("python-levenshtein") is None:
    os.system(f"%pip install python-levenshtein") # Not a standard library of Azure Machine Learning

# Imports
import pandas as pd
from thefuzz import fuzz

#Configuration
min_probability = 90 # Set to None if wanting to prompt user, otherwise, set between 0 and 100 with 100 representing an exact match
logging_level = 2 # 0=Errors, 1=Errors and Warnings, 2=Errors, Warnings, and Informational, 3=Errors, Warnings, Informational, and Debug
source_material_filter = ['Appliances','Drywall','Non Volatile Lumber','Volatile Lumber TRL','Volatile Lumber NTRL','Windows']

#Models
class Match:
    def __init__(self, id, probability):
        self.id = id
        self.probability = probability

class Material:
    def __init__(self, id, category, sub_category, name, is_generic):
        self.id = id
        self.category = category
        self.sub_category = sub_category
        self.name = name
        self.is_generic = is_generic

# Functions
def log(level, message): # levels: 0=Error, 1=Warning, 2=Information, 3=Debug
    if(level <= logging_level):
        print(message)

# The entry point function MUST have two input arguments.
# If the input port is not connected, the corresponding dataframe argument will be None.
#   dataframe1 and dataframe1 are of type pandas.DataFrame
def azureml_main(dataframe1 = None, dataframe2 = None):
    source_materials = []
    output_data = {
        "ItemCategory": [],
        "ItemSubCategory": [],
        "MatchProbability": [],
        "ItemName": [],
        "MatchingItemName": []
    }
    for index, row in dataframe1.iterrows():
        source_material = Material(row.ItemID, row.ItemCategory, row.ItemSubCategory, row.ItemName, row.IsGeneric)
        message = f"Category={source_material.category}\nSubCategory={source_material.sub_category}\nName={source_material.name}\n"
        possibleMatches = 0
        # Loop through all other materials comparing them to the current source material
        for compare_material in source_materials:
            if source_material.category in source_material_filter \
                and source_material.category==compare_material.category \
                and source_material.sub_category==compare_material.sub_category \
                and source_material.is_generic==compare_material.is_generic:
                probability = fuzz.ratio(source_material.name, compare_material.name) # pre-trained model using levenshtein distance algorithn
                if probability >= min_probability:
                    possibleMatches += 1
                    message += f"    probability={str(probability)}, name={compare_material.name}\n"
                    output_data["ItemCategory"].append(source_material.category)
                    output_data["ItemSubCategory"].append(compare_material.sub_category)
                    output_data["MatchProbability"].append(probability)
                    output_data["ItemName"].append(source_material.name)
                    output_data["MatchingItemName"].append(compare_material.name)
        if(logging_level >= 3 and possibleMatches > 0):
            print(message)
        source_materials.append(source_material)
    output_dataframe = pd.DataFrame(output_data)
    return output_dataframe
