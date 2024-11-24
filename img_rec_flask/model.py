from torch import nn
import torch

class CNNModel(nn.Module):
    def __init__(self, input_shape, hidden_units):
        super(CNNModel, self).__init__()
        self.fc1 = nn.Linear(input_shape, hidden_units)
        self.fc2 = nn.Linear(hidden_units, 1)  

    def forward(self, x):
        x = x.view(x.size(0), -1)  
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x  