import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from statsmodels.tsa.arima.model import ARIMA
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DiscrepancyPredictionEngine:
    """
    Predicts imbalances before they occur.
    """
    
    def __init__(self):
        self.model_gb = GradientBoostingRegressor()
        self.model_arima = None
        self.is_trained = False
        
    def train(self, features: pd.DataFrame, target: pd.Series):
        """
        Train the Gradient Boosting model.
        """
        self.model_gb.fit(features, target)
        self.is_trained = True
        
    def predict(self, features: pd.DataFrame) -> np.ndarray:
        """
        Predict the probability of an arbitrage opportunity.
        """
        if not self.is_trained:
            raise Exception("Model not trained")
        return self.model_gb.predict(features)
    
    def train_arima(self, time_series: pd.Series):
        """
        Train an ARIMA model on a time series of price discrepancies.
        """
        self.model_arima = ARIMA(time_series, order=(5,1,0))
        self.model_arima_fit = self.model_arima.fit()
        
    def forecast_arima(self, steps: int) -> pd.Series:
        """
        Forecast the next steps using the ARIMA model.
        """
        if self.model_arima_fit is None:
            raise Exception("ARIMA model not trained")
        return self.model_arima_fit.forecast(steps=steps)