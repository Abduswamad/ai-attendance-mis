class TimeInTimeOutDataAnalyzer:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def summarize_data(self):
        summary = self.dataframe.describe()
        return summary

    def feature_engineering(self,  target='Id Number'):
        # Extract features from timein
        self.dataframe['day_of_week'] = self.dataframe['time_in'].dt.dayofweek
        self.dataframe['hour_of_day'] = self.dataframe['time_in'].dt.hour
        # Add duration as a feature
        self.dataframe['duration'] = (self.dataframe['time_out'] - self.dataframe['time_in']).dt.total_seconds() / 60.0

        # Define features and target
        features = ['day_of_week', 'hour_of_day', 'duration']

        return self.dataframe

