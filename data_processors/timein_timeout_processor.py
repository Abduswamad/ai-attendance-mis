import pandas as pd


class TimeInTimeOutDataProcessor:
    def __init__(self, data):
        self.dataframe = pd.DataFrame(data)

    def process_data(self):
        self.dataframe['time_in'] = pd.to_datetime(self.dataframe['time_in'])
        self.dataframe['time_out'] = pd.to_datetime(self.dataframe['time_out'])
        return self.dataframe





