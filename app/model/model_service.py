"""This file is used to service the Trained Model."""

import pickle as pk
from os.path import exists, join
from typing import Optional

from loguru import logger

from app.config.model_config import model_settings
from app.model.pipeline.model import build_model


class ModelService:
    """This class is used to serve trained model."""

    def __init__(self):
        """Init Method of the class."""
        self.regressor = None

    def load_model(
        self,
        model_name: Optional[str] = model_settings.model_name,
    ) -> None:
        """
        Load model from the given location.

        :param model_name: Model name, defaults to model_settings.model_name
        :type model_name: Optional[str]
        """
        logger.info('Loading the model !!')
        model_path = join(model_settings.model_dir, model_name)
        logger.debug(f'Model name: {model_name} and Model path: {model_path}')
        if not exists(model_path):
            logger.warning(
                f'No model found at path: {model_path}, '
                + 'rebuilding the model !!',
            )
            build_model()

        with open(model_path, 'rb') as fp:
            self.regressor = pk.load(fp)
        logger.info('Model loaded Successfully !!')

    def predict(self, input_parameters: list) -> float:
        """
        Infer runs scored in 2019 using input parameters.

        :param input_parameters: Input parameters (features).
        :type input_parameters: list
        :return: Runs scored
        :rtype: float
        """
        logger.info('Starting model prediction for the given input !!')
        logger.debug(f'Input for prediction: {input_parameters}')
        prediction = self.regressor.predict([input_parameters])
        logger.info('Predicted Successfully for the input !!')
        return prediction
