"""Sentiment prediction module using trained ML model."""

import pickle
import os
from utils import clean_text

class SentimentPredictor:
    """Load and manage sentiment prediction model."""
    
    def __init__(self):
        """Initialize the predictor with trained model and vectorizer."""
        try:
            model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
            vectorizer_path = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")
            
            if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
                raise FileNotFoundError(
                    "Model files not found. Please run train_model.py first."
                )
            
            self.model = pickle.load(open(model_path, "rb"))
            self.vectorizer = pickle.load(open(vectorizer_path, "rb"))
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")
    
    def predict(self, review_text):
        """Predict sentiment for a given review.
        
        Args:
            review_text: The review text to analyze
            
        Returns:
            dict: {'sentiment': 'Positive' or 'Negative', 'score': 0 or 1}
        """
        try:
            clean_review = [clean_text(review_text)]
            features = self.vectorizer.transform(clean_review).toarray()
            prediction = self.model.predict(features)[0]
            
            return {
                'sentiment': 'Positive' if prediction == 1 else 'Negative',
                'score': prediction
            }
        except Exception as e:
            raise Exception(f"Prediction error: {str(e)}")


# Global predictor instance
_predictor = None

def get_predictor():
    """Get or create the global predictor instance."""
    global _predictor
    if _predictor is None:
        _predictor = SentimentPredictor()
    return _predictor


def predict_review(text):
    """Legacy function for backward compatibility."""
    predictor = get_predictor()
    result = predictor.predict(text)
    return result['sentiment']