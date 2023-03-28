# This module allows for checking an input material name against all existing materials
# Imports
import csv
from thefuzz import fuzz

# Configuration
input_file = "../inputs/materials.csv"

# Models
class Match:
    def __init__(self, id, name, probability):
        self.id = id
        self.name = name
        self.probability = probability

# Functions
def read_csv_file(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = []
        for row in reader:
            data.append(row)
    return header, data

# For this demo we only use name, but a new material would first select category and sub-category
inputName = input("\nInput name of new material: ")
# Read CSV data file
header, data = read_csv_file(input_file)

matches = []
for material in data:
    probability = fuzz.ratio(inputName, material[3])
    match = Match(material[0], material[3], probability)
    matches.append(match)
matches.sort(key=lambda x: x.probability, reverse=True)

for i in range(0,min(10, len(matches))):
    print("probability: " + str(matches[i].probability) + ", name=" + matches[i].name)
