from flask import Flask, render_template, request
import pickle
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('rf_model.pkl', 'rb'))

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form values
        temperature = float(request.form['temparature'])
        dewpoint = float(request.form['dewpoint'])
        humidity = float(request.form['humidity'])
        cloud = float(request.form['cloud'])
        winddirection = float(request.form['winddirection'])
        windspeed = float(request.form['windspeed'])

        # Prepare input for the model
        input_data = pd.DataFrame([[
            temperature, dewpoint, humidity, cloud, winddirection, windspeed
        ]], columns=['temparature', 'dewpoint', 'humidity', 'cloud', 'winddirection', 'windspeed'])

        # Make prediction
        prediction = model.predict(input_data)[0]
        label_map = {0: "No rain", 1: "Light rain", 2: "Heavy rain"}
        predicted_label = label_map[prediction]

        # Return result to HTML
        return render_template('index.html', prediction=predicted_label)

    except Exception as e:
        return f"Error during prediction: {str(e)}"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
