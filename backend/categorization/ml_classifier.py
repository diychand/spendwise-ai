import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

MODEL_PATH = os.path.join(os.path.dirname(__file__), "ml_model.joblib")
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), "vectorizer.joblib")


def train_model(descriptions, categories):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(descriptions)

    model = LinearSVC()
    model.fit(X, categories)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

    return model, vectorizer


def load_model():
    if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        return model, vectorizer
    return None, None


def predict_category(description, model, vectorizer):
    X = vectorizer.transform([description])
    prediction = model.predict(X)
    return prediction[0]