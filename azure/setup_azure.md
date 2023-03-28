# Azure Machine Learning Setup

1. Create an Azure Machine Learning Compute instance and in the `Advanced Settings` screen enable the idle shutdown

2. Create Azure Machine Learning Data Asset

3. Create Azure Machine Learning Designer uploading the file named `materials.csv`
    * This step can be skipped if connecting directly to source SQL database

4. Add the component named `Execute Python Script` and set the output from the data set to the input for the Python script

5. Use the code in file `azure_match.py` from this project as the code to execute in the designer

For production, the AML `Data Asset` would most likely be changed to an AML Datastore of type Azure SQL database using the managed identity of the workspace for access.
