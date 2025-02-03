import tensorflow as tf

def load_model(model_path):
    return tf.keras.models.load_model(model_path)

def predict_vulnerabilities(model, data):
    predictions = model.predict(data)
    vulnerabilities = ["SQL Injection", "XSS", "SSRF"]  # Example vulnerabilities based on predictions
    return vulnerabilities
