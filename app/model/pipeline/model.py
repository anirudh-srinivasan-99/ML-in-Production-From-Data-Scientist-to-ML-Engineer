from os.path import join
from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import xgboost
import pickle as pk

from app.model.pipeline.preparation import prepare_data
from app.config.config import settings
from loguru import logger

def build_model():
    logger.info("Starting build_model() function !!")
    df = prepare_data()
    logger.info("Prepared date for training !!")
    X_train, Y_train = get_features_and_target(df)
    x_train, x_test, y_train, y_test = get_train_test_split(X_train, Y_train)

    regressor = train_model(x_train, y_train)
    logger.info("Trained the Model !!")
    eval_score = evaluate_model(regressor, x_test, y_test)
    logger.info(f"Evaluation Score for the model is {eval_score}")
    save_model(regressor)
    logger.info("Saved model to ")
    logger.info("Completed build_model() function !!")

def get_features_and_target(
    df: pd.DataFrame, feat_cols: list = [
        'Mat', 'Inns', '2018_Runs', 'HS', 
        'Avg', 'BF', 50, '4s', '6s'
    ], target_col = '2019_Runs'
):
    return df[feat_cols], df[target_col]

def get_train_test_split(
    X_train: pd.DataFrame, Y_train: pd.Series
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:

    x_train, x_test, y_train, y_test = train_test_split(
        X_train, Y_train, random_state = 1
    )
    return x_train, x_test, y_train, y_test

def train_model(
    x_train: pd.DataFrame, y_train: pd.Series
) -> xgboost.XGBRegressor:
    logger.info("Model Training Starts !!")
    grid_space = {
        'n_estimators': [100, 500, 900, 1100, 1500],
        'max_depth': [2, 3, 5, 10, 15],
        'learning_rate': [0.05,0.1,0.15,0.20],
        'min_child_weight': [1,2,3,4],
        'booster': ['gbtree','gblinear'],
        'base_score': [0.25,0.5,0.75,1]
    }
    logger.info("Grid Space Initialized !!")
    grid = GridSearchCV(
        xgboost.XGBRegressor(), 
        param_grid=grid_space, n_jobs=5,
        cv=5, scoring = 'r2', verbose=True
    )

    best_grid_model = grid.fit(x_train, y_train)
    logger.info("Model with best fit optained !!")
    logger.info("Model Training Completed !!")
    return best_grid_model.best_estimator_

def evaluate_model(
    regressor: xgboost.XGBRegressor, x_test: pd.DataFrame, 
    y_test: pd.Series
) -> float:
    return regressor.score(x_test, y_test)

def save_model(
    regressor: xgboost.XGBRegressor
):
    save_path = join(settings.model_dir, settings.model_name)
    with open(save_path, 'wb') as f:
        pk.dump(regressor, f)
    logger.info(f"Saved model to {save_path}")
