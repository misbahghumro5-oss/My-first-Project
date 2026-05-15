import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("data.csv")

X = data[['duration', 'packets', 'failed_logins']]
y = data['label']

model = RandomForestClassifier()
model.fit(X, y)

def predict_attack(duration, packets, failed_logins):
    input_data = [[duration, packets, failed_logins]]
    prediction = model.predict(input_data)
    return prediction[0]