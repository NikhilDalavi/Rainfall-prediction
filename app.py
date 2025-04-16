
# from flask import Flask, render_template, request
# import pickle
# import numpy as np

# app = Flask(__name__)
# model = pickle.load(open("rf_model.pkl", "rb"))

# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get input values from form
#         inputs = [
#             float(request.form['day']),
#             float(request.form['pressure']),
#             float(request.form['maxtemp']),
#             float(request.form['temparature']),
#             float(request.form['mintemp']),
#             float(request.form['dewpoint']),
#             float(request.form['humidity']),
#             float(request.form['cloud']),
#             float(request.form['sunshine']),
#             float(request.form['winddirection']),
#             float(request.form['windspeed']),
#         ]
#         prediction = model.predict([inputs])[0]
#         label = {0: "No Rain", 1: "Light Rain", 2: "Heavy Rain"}.get(prediction, "Unknown")
#         return render_template("index.html", prediction=f"Predicted Rainfall: {label}")
#     except Exception as e:
#         return render_template("index.html", prediction=f"Error: {str(e)}")

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request
# import pickle
# import pandas as pd

# app = Flask(__name__)


# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         features = [float(request.form.get(field)) for field in ['temparature', 'dewpoint', 'humidity', 'cloud', 'winddirection', 'windspeed']]
#         input_data = pd.DataFrame([features], columns=['temparature', 'dewpoint', 'humidity', 'cloud', 'winddirection', 'windspeed'])
        
#         model = pickle.load(open('rf_model.pkl', 'rb'))
#         pred = model.predict(input_data)[0]
#         label_map = {0: "No rain", 1: "Light rain", 2: "Heavy rain"}
#         prediction = label_map[pred]

#         return render_template('your_template.html', prediction=prediction)
#     except Exception as e:
#         return f"Error: {str(e)}"

from flask import Flask, render_template, request
import pickle
import pandas as pd
import os  # Required for Render port handling

app = Flask(__name__)

# Load the model only once when app starts (faster)
model = pickle.load(open('rf_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')  # Make sure your HTML file is named 'index.html'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form.get(field)) for field in ['temparature', 'dewpoint', 'humidity', 'cloud', 'winddirection', 'windspeed']]
        input_data = pd.DataFrame([features], columns=['temparature', 'dewpoint', 'humidity', 'cloud', 'winddirection', 'windspeed'])

        pred = model.predict(input_data)[0]
        label_map = {0: "No rain", 1: "Light rain", 2: "Heavy rain"}
        prediction = label_map[pred]

        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return f"Error: {str(e)}"

# Required for Render: run on port from environment variable
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


