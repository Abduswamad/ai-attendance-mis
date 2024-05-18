import pandas as pd


class TimeinTimeoutDataPreprocessor:
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def clean_data(self):
        self.df['timein'] = pd.to_datetime(self.df['timein'])
        self.df['timeout'] = pd.to_datetime(self.df['timeout'])
        self.df['duration'] = self.df['timeout'] - self.df['timein']
        return self.df