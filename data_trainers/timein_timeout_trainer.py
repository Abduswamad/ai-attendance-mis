from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd


class TimeInTimeOutTrainer:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.model = None
        self.features = ['day_of_week', 'hour_of_day', 'duration']
        self.target_column = 'Id Number'

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(
            self.dataframe[self.features],
            self.dataframe[self.target_column],
            test_size=0.2, random_state=42
        )

        # Train the model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model accuracy: {accuracy * 100:.2f}%")

    def predict_id(self, time_in, time_out):
        """
                Predict the ID number based on time in and time out.

                :param time_in: str or pd.Timestamp, the time in
                :param time_out: str or pd.Timestamp, the time out
                :return: predicted ID number
                """
        # Convert to datetime
        time_in = pd.to_datetime(time_in)
        time_out = pd.to_datetime(time_out)

        # Create a DataFrame with the features
        data = {
            'day_of_week': [time_in.dayofweek],
            'hour_of_day': [time_in.hour],
            'duration': [(time_out - time_in).total_seconds() / 60.0]
        }
        input_df = pd.DataFrame(data)

        # Predict
        if self.model is not None:
            prediction = self.model.predict(input_df)
            return prediction[0]
        else:
            raise ValueError("Model is not trained yet. Please train the model before prediction.")





