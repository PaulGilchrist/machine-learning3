# machine-learning

This project has several example of Machine Learning scripts and notebooks used for learning the basics of deep learning neural networks.

## Machine Learning Summarized

In machine learning, the equation `y = x*w+b` is used to predict the value of y given the input x, where the weights (w) and biases (b) are learned through multiple iterations (epochs) of training on a complete set of training data. In each epoch, the actual value of y is compared against the predicted value to determine the loss. This loss is then combined with the optimizer's learning rate to calculate gradients (derivatives), which provide the direction and magnitude of the steepest ascent or descent. These gradients are used in the next epoch to adjust the weights and biases, bringing the predicted values closer to the actual values. After training is complete, the final values of the weights and biases make up the model algorithm that can be used to predict y from x as `y = model(x)`.

In machine learning, all data must be in numeric form. This means that words are either directly converted to unique indexes, or first converted to characters, which are then serialized through the training. Similarly, enumerations or categories must be converted to binary representation. If only two states exist, they can be converted directly to binary. Otherwise, "one hot encoding" is used, which represents each category as its own variable with 1 indicating the presence of a category and 0 indicating its absence. This conversion is necessary to ensure that the data can be processed by the machine learning algorithm, and allows the algorithm to use mathematical operations to extract patterns and make accurate predictions.

All of these machine learning specific terms are explained in more detail in the file named `terminology.md`

## Python Scripts in this Project

### api

* `app.py` Api that leverages the model created by the 'home_prices.ipynb' notebook, showing how to recieve an HTTP POST action with JSON body send it through the model, and return back a price prediction.

### azure

* `azure_match.py` can be used with Azure Machine Learning's (AML) `Execute Python Script` functionality and will compare every material passes in as dataframe1, against every other material, generating an output dataframe of all the matches above a configurable probability.  
* `match_all.py` allows for local development and debugging of the AML script using this project's `./inputs/materials.csv` file as input and producing `./outputs/material_matches.csv` as output, replacing AML's Panda datasets as inputs and outputs.
    * Test data includes 55,387 materials, takes 1,533,832,191 comparisons, and at a minimum probability of 90% returns 748,205 suspected matches.  This drops to 232,768 suspected matches at 95% probability and 16,078 possible matches at 99% probability.
    * This script can process all 1.5 billion comparison datasets in < 4.5 minutes on Macbook M1 Pro.  In AML running on a compute instance of size `STANDARD_DS11_V2`, the time roughly doubles to < 9 minutes.
* `match.py` compares a new material names entered against all existing materials, and returns the top 5 matches.  This could be used in an application to prevent duplicate materials from being added, allowing the user to instead see that an existing suitable material already exists.

### notebooks

* `classification_image.ipynb` Demo to classify images based on the type of clothing being worn in the image
* `classification_multi.ipynb` Demo to classify which passengers of the Titanic would survive using multiple inputs
* `classification_text.ipynb` Demo to classify which English names are female vs male (single input)
* `fidelity.ipynb` Demo showing multi-input prediction training sources from multiple soure dataframes. This demo also shows how to handle ordered categories.
* `home-prices.ipynb` Demo showing multi-input prediction training with very large categories requiring embeddings instead of one hot encoding.
* `language_analogies.ipynb` Demo to using pretrained Glove model of word distances to use for finding similar words or words used frequently together
* `language_translation.ipynb` Demo of German to English language translation
* `regression_single.ipynb` Demo to calculate a linear regression with graphical output
* `regression_multi.ipynb` Demo to calculate the pricing of automobiles based on multiple inputs

All notebooks graphically display a convergance chart to help with determining the best number of epochs and learning rates.  Notebooks also show final model accuracy, and examples of saving, loading, and using trained models.

## Notes

* Review the `documents` folder of this project for more information.
* Jupyter notebooks can all be found in the `notebooks` folder.
* conda update --all