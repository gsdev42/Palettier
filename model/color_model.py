import joblib
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class ColorSeasonModel:
    def __init__(self):
        """Initialize the color season classifier with default parameters"""
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=5,
            random_state=42,
            class_weight='balanced'
        )
        self.label_encoders = {
            'undertone': LabelEncoder(),
            'hair_color': LabelEncoder(),
            'eye_color': LabelEncoder(),
            'saturation': LabelEncoder()
        }
        self.classes_ = None
        self.feature_importances_ = None

    def train(self, data_path="data.csv", model_save_path="model.pkl", test_size=0.2):
        """
        Train and save the model
        Args:
            data_path (str): Path to training data CSV
            model_save_path (str): Path to save trained model
            test_size (float): Fraction of data to use for validation (0-1)
        """
        # Verify data file exists
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Training data not found at {data_path}")

        df = pd.read_csv(data_path)

        # Fit label encoders
        for col in self.label_encoders:
            self.label_encoders[col].fit(df[col])

        # Prepare features and target
        X = df[['undertone', 'hair_color', 'eye_color', 'saturation']]
        y = df['season']

        # Encode features
        X_encoded = self._encode_features(X)

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X_encoded, y, test_size=test_size, random_state=42)

        # Train model
        self.model.fit(X_train, y_train)
        self.classes_ = self.model.classes_
        self.feature_importances_ = self.model.feature_importances_

        # Validate
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model trained with validation accuracy: {accuracy:.2f}")

        # Save model
        self.save_model(model_save_path)
        return accuracy

    def _encode_features(self, features):
        """Encode categorical features using fitted encoders"""
        encoded = features.copy()
        for col in self.label_encoders:
            if col in features.columns:
                encoded[col] = self.label_encoders[col].transform(features[col])
        return encoded

    def save_model(self, path="model.pkl"):
        """Serialize model to disk with all components"""
        # Only create directory if path contains subdirectories
        dir_path = os.path.dirname(path)
        if dir_path:  # Only if path contains directories
            os.makedirs(dir_path, exist_ok=True)

        joblib.dump({
            'model': self.model,
            'label_encoders': self.label_encoders,
            'classes': self.classes_,
            'feature_importances': self.feature_importances_
        }, path)

    @classmethod
    def load_model(cls, path="model.pkl"):
        """Load serialized model from disk"""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Model file not found at {path}")

        data = joblib.load(path)
        model = cls()
        model.model = data['model']
        model.label_encoders = data['label_encoders']
        model.classes_ = data.get('classes')
        model.feature_importances_ = data.get('feature_importances')
        return model

    def predict(self, features):
        """
        Predict color season from input features
        Args:
            features (dict): {
                'undertone': str,
                'hair_color': str,
                'eye_color': str,
                'saturation': str
            }
        Returns:
            str: Predicted season
        """
        X = pd.DataFrame([features])
        X = self._encode_features(X)
        return self.model.predict(X)[0]


