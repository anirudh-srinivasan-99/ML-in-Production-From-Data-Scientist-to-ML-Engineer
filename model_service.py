from os.path import join, exists
import pickle as pk

from model import build_model
from config import settings

class ModelService:
    def __init__(self):
        self.regressor = None
    
    def load_model(self, model_name=settings.model_name):
        model_path = join(settings.model_dir, settings.model_name)

        if not exists(model_path):
            build_model()

        self.regressor = pk.load(open(model_path, 'rb'))

    def predict(self, input_parameters: list) -> float:
        return self.regressor.predict([input_parameters])