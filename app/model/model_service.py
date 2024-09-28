from os.path import join, exists
import pickle as pk

from app.model.pipeline.model import build_model
from app.config.config import settings
from loguru import logger


class ModelService:
    def __init__(self):
        self.regressor = None
    
    def load_model(self, model_name=settings.model_name):
        logger.info("Loading the model !!")
        model_path = join(settings.model_dir, model_name)
        logger.debug(f"Model name: {model_name} and Model path: {model_path}")
        if not exists(model_path):
            logger.warning(
                f"No model found at path: {model_path}, "
                "rebuilding the model !!"
            )
            build_model()

        self.regressor = pk.load(open(model_path, 'rb'))
        logger.info("Model loaded Successfully !!")

    def predict(self, input_parameters: list) -> float:
        logger.info("Starting model prediction for the given input !!")
        logger.debug(f"Input for prediction: {input_parameters}")
        prediction = self.regressor.predict([input_parameters])
        logger.info("Predicted Successfully for the input !!")
        return prediction