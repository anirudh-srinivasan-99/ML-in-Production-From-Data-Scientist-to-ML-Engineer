from pathlib import Path
import pickle as pk

from model import build_model

class ModelService:
    def __init__(self):
        self.regressor = None
    
    def load_model(self, model_name='xgr_v1'):
        model_path = Path(f'models/{model_name}')

        if not model_path.exists():
            build_model()

        self.regressor = pk.load(open(f'models/{model_name}', 'rb'))

    def predict(self, input_parameters: list) -> float:
        return self.regressor.predict([input_parameters])