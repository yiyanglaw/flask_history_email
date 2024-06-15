from flask import Flask, request, jsonify

app = Flask(__name__)

# Placeholder function for spam prediction
def predict_spam(text):
    # Implement your spam prediction logic here
    # For now, we'll just return a dummy result
    return "Spam" if "spam" in text.lower() else "Not Spam"

# Function to write text and prediction to history files
def write_to_history(file_name, text, prediction):
    with open(file_name, 'a') as file:
        file.write(f"Text: {text}\nPrediction: {prediction}\n\n")

# Route for email spam prediction
@app.route('/email/predict_spam', methods=['POST'])
def predict_email_spam():
    text = request.form['text']
    prediction = predict_spam(text)
    write_to_history('history_email.txt', text, prediction)
    return jsonify({"text": text, "prediction": prediction})

# Route for SMS spam prediction
@app.route('/sms/predict_spam', methods=['POST'])
def predict_sms_spam():
    text = request.form['text']
    prediction = predict_spam(text)
    write_to_history('history_sms.txt', text, prediction)
    return jsonify({"text": text, "prediction": prediction})

# Route to display email history
@app.route('/email/history', methods=['GET'])
def email_history():
    try:
        with open('history_email.txt', 'r') as file:
            content = file.read()
        return jsonify({"history": content}), 200
    except FileNotFoundError:
        return jsonify({"error": "History file not found"}), 404

# Route to display SMS history
@app.route('/sms/history', methods=['GET'])
def sms_history():
    try:
        with open('history_sms.txt', 'r') as file:
            content = file.read()
        return jsonify({"history": content}), 200
    except FileNotFoundError:
        return jsonify({"error": "History file not found"}), 404

@app.route('/')
def home():
    return "Welcome to the Spam Classification Service!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10004, debug=False)
