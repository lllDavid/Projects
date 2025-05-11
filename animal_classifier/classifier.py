from os import path
from PIL import Image
from model import Model
from pathlib import Path
from torchvision import transforms
from torch import device, cuda, no_grad, load, sigmoid

class Classifier:
    def main(self, image_path):
        device_type = device("cuda" if cuda.is_available() else "cpu")

        input_shape = 128 * 128 * 3
        hidden_units = 1024

        MODEL_PATH = Path("saved_models") / "Model.pth"
        loaded_model = Model(input_shape=input_shape, hidden_units=hidden_units)
        loaded_model.load_state_dict(load(MODEL_PATH, map_location=device_type, weights_only=True))
        loaded_model.eval()
        loaded_model.to(device_type)

        transform = transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])

        def predict_image(image_path, model, transform):
            image = Image.open(image_path).convert('RGB')
            image = transform(image).unsqueeze(0).to(device_type)

            with no_grad():
                logits = model(image)
                prediction = sigmoid(logits).item() > 0.5 
            return prediction
        
        result = predict_image(image_path, loaded_model, transform)

        resultString = f"The image {path.basename(image_path)} is a {'cat' if result else 'dog'}."
        return resultString
