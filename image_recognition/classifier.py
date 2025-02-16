import os
import torch
from PIL import Image
from pathlib import Path
from model import CNNModel
from torchvision import transforms

class Classifier:
    def main(self, image_path):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        input_shape = 128 * 128 * 3
        hidden_units = 1024

        MODEL_PATH = Path("saved_models") / "CNNModel.pth"
        loaded_model = CNNModel(input_shape=input_shape, hidden_units=hidden_units)
        loaded_model.load_state_dict(torch.load(MODEL_PATH, map_location=device, weights_only=True))
        loaded_model.eval()
        loaded_model.to(device)

        transform = transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])

        def predict_image(image_path, model, transform):
            image = Image.open(image_path).convert('RGB')
            image = transform(image).unsqueeze(0).to(device)

            with torch.no_grad():
                logits = model(image)
                prediction = torch.sigmoid(logits).item() > 0.5 
            return prediction
        
        result = predict_image(image_path, loaded_model, transform)

        resultString = f"The image {os.path.basename(image_path)} is a {'cat' if result else 'dog'}."
        return resultString
