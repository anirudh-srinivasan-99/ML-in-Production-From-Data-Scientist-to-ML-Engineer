"""This file is used to build the model using the IPL Data."""
import pickle as pk
from os.path import join
from typing import Tuple

import pandas as pd
import xgboost
from loguru import logger
from sklearn.model_selection import GridSearchCV, train_test_split

from app.config.model_config import model_settings
from app.model.pipeline.preparation import prepare_data


def build_model():  # noqa: WPS210
    """Build the model by preparing the dataset and training the model."""
    logger.info('Starting build_model() function !!')
    df = prepare_data()
    logger.info('Prepared date for training !!')
    feature_columns = [  # noqa: WPS317
        'Mat', 'Inns', '2018_Runs', 'HS',
        'Avg', 'BF', 50, '4s', '6s',
    ]
    target_column = '2019_Runs'
    X_train, Y_train = _get_features_and_target(
        df, feature_columns, target_column,
    )  # noqa: N806
    x_train, x_test, y_train, y_test = _get_train_test_split(X_train, Y_train)

    regressor = _train_model(x_train, y_train)
    logger.info('Trained the Model !!')
    eval_score = _evaluate_model(regressor, x_test, y_test)
    logger.info(f'Evaluation Score for the model is {eval_score}')
    _save_model(regressor)
    logger.info('Completed build_model() function !!')


def _get_features_and_target(
    df: pd.DataFrame,
    feat_cols: list,
    target_col: str,
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Distinguish between attributes and target.

    :param df: Data to be trained/ tested on.
    :type df: pd.DataFrame
    :param feat_cols: Feature Columns
    :type feat_cols: list
    :param target_col: Target Column
    :type target_col: str
    :return: Attributes and the Target Variable.
    :rtype: Tuple[pd.DataFrame, pd.Series]
    """
    return df[feat_cols], df[target_col]


def _get_train_test_split(
    X_train: pd.DataFrame, Y_train: pd.Series,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Split the data into training and testing data.

    :param X_train: Attributes
    :type X_train: pd.DataFrame
    :param Y_train: Target feature.
    :type Y_train: pd.Series
    :return: Training and Testing Data
    :rtype: Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]
    """
    x_train, x_test, y_train, y_test = train_test_split(
        X_train, Y_train, random_state=1,
    )
    return x_train, x_test, y_train, y_test  # noqa: WPS331


def _train_model(
    x_train: pd.DataFrame, y_train: pd.Series,
) -> xgboost.XGBRegressor:
    """
    Train the model, using the training data provided.

    :param x_train: Training Attributes
    :type x_train: pd.DataFrame
    :param y_train: Training Feature
    :type y_train: pd.Series
    :return: Best Model given the model search space.
    :rtype: xgboost.XGBRegressor
    """
    logger.info('Model Training Starts !!')
    grid_space = {
        'n_estimators': [100, 500, 900, 1100, 1500],
        'max_depth': [2, 3, 5, 10, 15],
        'learning_rate': [0.05, 0.1, 0.15, 0.20],
        'min_child_weight': [1, 2, 3, 4],
        'booster': ['gbtree', 'gblinear'],
        'base_score': [0.25, 0.5, 0.7, 1],
    }
    logger.info('Grid Space Initialized !!')
    grid = GridSearchCV(
        xgboost.XGBRegressor(),
        param_grid=grid_space,
        n_jobs=5,
        cv=5,
        scoring='r2',
        verbose=True,
    )

    best_grid_model = grid.fit(x_train, y_train)
    logger.info('Model with best fit optained !!')
    logger.info('Model Training Completed !!')
    return best_grid_model.best_estimator_


def _evaluate_model(
    regressor: xgboost.XGBRegressor,
    x_test: pd.DataFrame,
    y_test: pd.Series,
) -> float:
    """
    Evaluate the trained model using the test dataset.

    :param regressor: Model
    :type regressor: xgboost.XGBRegressor
    :param x_test: Test Attributes
    :type x_test: pd.DataFrame
    :param y_test: Test Target Feature
    :type y_test: pd.Series
    :return: Evaluation Score from 0 to 1,
        where 1 implies perfect match
    :rtype: float
    """
    return regressor.score(x_test, y_test)


def _save_model(
    regressor: xgboost.XGBRegressor,
):
    """
    Save the trained model.

    :param regressor: Trained Model
    :type regressor: xgboost.XGBRegressor
    """
    save_path = join(model_settings.model_dir, model_settings.model_name)
    with open(save_path, 'wb') as fp:
        pk.dump(regressor, fp)
    logger.info(f'Saved model to {save_path}')
