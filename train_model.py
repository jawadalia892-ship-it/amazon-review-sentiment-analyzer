"""Train sentiment classification model using SVM and TF-IDF."""

import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report
from utils import clean_text

def load_dataset(filepath="dataset.csv"):
    """Load and validate dataset."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found: {filepath}")
    
    data = pd.read_csv(filepath)
    
    if 'Review' not in data.columns or 'Label' not in data.columns:
        raise ValueError("Dataset must have 'Review' and 'Label' columns")
    
    print(f"✓ Loaded {len(data)} reviews from {filepath}")
    return data

def preprocess_data(data):
    """Clean and preprocess text data."""
    print("\n📝 Preprocessing text...")
    data['Review'] = data['Review'].apply(clean_text)
    return data

def create_features(data):
    """Create TF-IDF features."""
    print("🔧 Creating TF-IDF features...")
    cv = TfidfVectorizer(
        max_features=200,
        ngram_range=(1, 2),
        min_df=1,
        max_df=0.9
    )
    X = cv.fit_transform(data['Review']).toarray()
    y = data['Label']
    
    print(f"   - Features created: {X.shape}")
    return X, y, cv

def train_model(X, y):
    """Train LinearSVC model."""
    print("\n🤖 Training LinearSVC model...")
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = LinearSVC(max_iter=2000, random_state=42, C=1.0)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"✓ Model trained successfully")
    print(f"\n📊 Accuracy: {accuracy:.2%}")
    print("\n📋 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=['Negative', 'Positive']))
    
    return model, X_test, y_test, y_pred

def save_model(model, vectorizer, model_path="model.pkl", vec_path="vectorizer.pkl"):
    """Save trained model and vectorizer."""
    print("\n💾 Saving model...")
    pickle.dump(model, open(model_path, "wb"))
    pickle.dump(vectorizer, open(vec_path, "wb"))
    print(f"✓ Model saved to {model_path}")
    print(f"✓ Vectorizer saved to {vec_path}")

def main():
    """Main training pipeline."""
    print("\n" + "="*50)
    print("  Sentiment Classification Model Training")
    print("="*50)
    
    try:
        # Load and preprocess
        data = load_dataset()
        data = preprocess_data(data)
        
        # Create features
        X, y, cv = create_features(data)
        
        # Train model
        model, X_test, y_test, y_pred = train_model(X, y)
        
        # Save model
        save_model(model, cv)
        
        print("\n✅ Training completed successfully!")
        print("="*50 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    main()