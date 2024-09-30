"""This file is the main runner file."""

from loguru import logger

from app.config.model_config import model_settings
from app.model.model_service import ModelService


def main():
    """Run the application."""
    logger.info('Starting main() function !!')
    ml_svc = ModelService()
    ml_svc.load_model(model_settings.model_name)
    logger.info('Loaded the model !!')
    pred = ml_svc.predict(
       [10, 9, 134, 46, 16.75, 100, 0, 6, 8],
    )
    logger.info(f'Module Prediction: {pred}')
    logger.info('Completed main() function !!')


if __name__ == '__main__':
    main()
