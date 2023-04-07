# The Azure Machine Learning scripts MUST contain a function named azureml_main which is the entry point for Azure Machine Learning
from flask import Flask, abort, jsonify, request
import torch
import torch.nn as nn
app = Flask(__name__)

# Example POST body JSON showing required inputs to predict a home price
# {
#   "brand": "Pulte Homes",
#   "zip": "48439",
#   "bedrooms": 4,
#   "baths": 2.5,
#   "baseSqFt": 3000,
#   "garage": 3,
#   "stories": 2
# }

# Define PyTorch model
class MyModel(nn.Module):
    def __init__(self, in_features, num_brand_embeddings, num_zip_embeddings, brand_dictionary, zip_dictionary):
        super(MyModel, self).__init__()
        embedding_dim = 10 # Size of each embedding vector (tunable during training)
        hidden_dim = 32 # Dimensions used for the inner layers of the model
        self.brand_dictionary = brand_dictionary
        self.zip_dictionary = zip_dictionary
        self.brand_embedding = nn.Embedding(num_brand_embeddings, embedding_dim)
        self.zip_embedding = nn.Embedding(num_zip_embeddings, embedding_dim)
        in_features = embedding_dim*2 + in_features
        self.layer1 = nn.Linear(in_features, hidden_dim*2)
        self.layer2 = nn.Linear(hidden_dim*2, hidden_dim)
        self.layer3 = nn.Linear(hidden_dim, 1)
        
    def forward(self, brand_tensor, zip_tensor, input_tensor):
        brand_tensor = self.brand_embedding(brand_tensor.to(torch.int))
        zip_tensor = self.zip_embedding(zip_tensor.to(torch.int))
        # Concat all tensors after creating embedding vectors, then pass them into the first layer
        # Input Tensor Index = baseSqFt, bedrooms, baths, garage, stories
        x = torch.cat([brand_tensor, zip_tensor, input_tensor], dim=1)
        x = nn.functional.relu(self.layer1(x))
        x = nn.functional.relu(self.layer2(x))
        x = self.layer3(x)
        return x

def get_key(dictionary, value):
    # The key is the embedding index, and the value is the category string
    for key, val in dictionary.items():
        if val == value:
            return key
    return -1 # Not found

@app.route('/predictPrice', methods=['POST'])
def predict():
    data = request.get_json()
    brand_embedding_index = get_key(model.brand_dictionary, data['brand'])
    if(brand_embedding_index == -1):
        abort(400, f'Unknown brand')
    brand_tensor = torch.tensor([brand_embedding_index], dtype=torch.long)
    zip_embedding_index = get_key(model.zip_dictionary, data['zip'])
    if(zip_embedding_index == -1):
        print(model.zip_dictionary)
        abort(400, f'Unknown zip')
    zip_tensor = torch.tensor([zip_embedding_index], dtype=torch.long)
    # remaining required inputs
    input_tensor = torch.tensor([[data['baseSqFt'], data['bedrooms'], data['baths'], data['garage'], data['stories']]], dtype=torch.float)
    prediction = model(brand_tensor, zip_tensor, input_tensor)
    return jsonify({'predicted_price': round(prediction.item())})

if __name__ == '__main__':
    model = torch.load('home_price_model_bhi.pth')
    model.eval() # Put the model in "evaluation mode", this turns off dropout and batch normalization.
    app.run(debug=True, host='0.0.0.0', port=80) # bind to all interfaces
