import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Sample data
data = [
    {"Id Number": "01", "timein": "2023-01-02 08:47:00", "timeout": "2023-01-02 09:00:00"},
    {"Id Number": "01", "timein": "2023-01-03 08:03:00", "timeout": "2023-01-03 17:02:00"}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert timein and timeout to datetime
df['timein'] = pd.to_datetime(df['timein'])
df['timeout'] = pd.to_datetime(df['timeout'])

# Extract features from timein
df['day_of_week'] = df['timein'].dt.dayofweek
df['hour_of_day'] = df['timein'].dt.hour

# Add duration as a feature
df['duration'] = (df['timeout'] - df['timein']).dt.total_seconds() / 60.0  # duration in minutes

# Define features and target
features = ['day_of_week', 'hour_of_day', 'duration']
target = 'Id Number'

# Split the data
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# Define a function to predict the Id Number based on input time
def predict_id(timein, timeout):
    # Convert to datetime
    timein = pd.to_datetime(timein)
    timeout = pd.to_datetime(timeout)

    # Create a DataFrame with the features
    data = {
        'day_of_week': [timein.dayofweek],
        'hour_of_day': [timein.hour],
        'duration': [(timeout - timein).total_seconds() / 60.0]
    }
    input_df = pd.DataFrame(data)

    # Predict
    prediction = model.predict(input_df)
    return prediction[0]


# Example prediction
predicted_id = predict_id("2023-01-04 08:00:00", "2023-01-04 17:00:00")
print(f"The predicted Id Number is: {predicted_id}")