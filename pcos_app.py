from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

try:
    with open('best_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading model:", e)


@app.route('/')
def home():
    return render_template('PCOS_Classifier.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collecting all 42 features from the form
    features = [request.form[key] for key in request.form.keys()]
    features = [float(x) if x.replace('.', '', 1).isdigit() else x for x in features]
    
    # Ensure the number of features matches the model's expectation
    if len(features) != 42:
        return render_template('PCOS_Classifier.html', result="Error: Incorrect number of features.")
    
    final_features = [np.array(features)]
    
    try:
        prediction = model.predict(final_features)
        output = 'Yes' if prediction[0] == 1 else 'No'
    except Exception as e:
        output = str(e)
    
    return render_template('PCOS_Classifier.html', result=output)

if __name__ == "__main__":
    app.run(debug=True)
