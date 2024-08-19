from flask import Flask, request, render_template
import numpy as np
import pickle
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Define the Flask application object
app = Flask(__name__)

# Load the trained model
try:
    with open('best_model.pkl', 'rb') as f:
        model = pickle.load(f)
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    model = None

@app.route('/')
def home():
    return render_template('PCOS_Classifier.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collecting all features from the form
        logging.debug(f"Form data received: {request.form}")
        features = [request.form[key] for key in request.form.keys()]
        logging.debug(f"Received {len(features)} features, expected 41.")

        # Define the categorical mapping
        categorical_map = {'Y': 1, 'N': 0}

        # Convert features: handle both numeric and categorical
        try:
            converted_features = []
            for feature in features:
                # Convert categorical features
                if feature in categorical_map:
                    converted_features.append(categorical_map[feature])
                else:
                    # Convert numeric features
                    converted_features.append(float(feature))
        except ValueError as e:
            logging.error(f"Non-numeric data error: {e}")
            return render_template('PCOS_Classifier.html', result="Error: Non-numeric data detected in numeric fields.")

        # Ensure the number of features matches the model's expectation
        expected_features = 41
        if len(converted_features) != expected_features:
            logging.error(f"Expected {expected_features} features, but got {len(converted_features)}.")
            return render_template('PCOS_Classifier.html', result=f"Error: Expected {expected_features} features, but got {len(converted_features)}.")

        # Prepare the features for prediction
        final_features = [np.array(converted_features)]
        logging.debug(f"Final features for prediction: {final_features}")

        # Prediction logic
        if model is not None:
            try:
                prediction = model.predict(final_features)
                if prediction[0] == 0:
                    output = "PCOS DETECTED"
                elif prediction[0] == 1:
                    output = "PCOS NOT DETECTED"
                logging.debug(f"Prediction result: {output}")
            except Exception as e:
                logging.error(f"Prediction error: {e}")
                output = "Error occurred during prediction."
        else:
            output = "Model not available."

        return render_template('PCOS_Classifier.html', result=output)

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return render_template('PCOS_Classifier.html', result="An unexpected error occurred.")

if __name__ == "__main__":
    app.run(debug=True)
