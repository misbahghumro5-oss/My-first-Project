from flask import Flask, render_template, request
from model import predict_attack

app = Flask(__name__)

def validate_data(duration, packets, failed_logins):
    if duration < 0 or packets < 0 or failed_logins < 0:
        return False
    return True

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    
    if request.method == 'POST':
        duration = int(request.form['duration'])
        packets = int(request.form['packets'])
        failed_logins = int(request.form['failed_logins'])

        if not validate_data(duration, packets, failed_logins):
            result = "Invalid Data!"
        else:
            prediction = predict_attack(duration, packets, failed_logins)
            
            if prediction == "attack":
                result = "⚠️ Cyber Attack Detected!"
            else:
                result = "✅ Normal Activity"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
    