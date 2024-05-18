import pandas as pd


class TimeinTimeoutDataPreprocessor:
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def clean_data(self, working_hours=8, timein_hour=8, timein_minute=0, timeout_hour=17, timeout_minute=0):
        self.df['timein'] = pd.to_datetime(self.df['timein'])
        self.df['timeout'] = pd.to_datetime(self.df['timeout'])
        self.df['duration'] = self.df['timeout'] - self.df['timein']
        # Determine Working Hours
        self.df['is_undertime'] = self.df['duration'].apply(lambda x: x.total_seconds() / 3600 < working_hours)
        self.df['is_ontime'] = self.df['duration'].apply(lambda x: x.total_seconds() / 3600 == working_hours)
        self.df['is_overtime'] = self.df['duration'].apply(lambda x: x.total_seconds() / 3600 > working_hours)
        # Determine Time In
        self.df['is_early_in'] = self.df['timein'].apply(
            lambda x: x < pd.Timestamp(year=x.year, month=x.month, day=x.day, hour=timein_hour, minute=timein_minute))
        self.df['is_ontime_in'] = self.df['timein'].apply(
            lambda x: x == pd.Timestamp(year=x.year, month=x.month, day=x.day, hour=timein_hour, minute=timein_minute))
        self.df['is_late_in'] = self.df['timein'].apply(
            lambda x: x > pd.Timestamp(year=x.year, month=x.month, day=x.day, hour=timein_hour, minute=timein_minute))
        # Determine Time Out
        self.df['is_early_out'] = self.df['timeout'].apply(
            lambda x: x < pd.Timestamp(year=x.year, month=x.month, day=x.day, hour=timeout_hour, minute=timeout_minute))
        self.df['is_ontime_out'] = self.df['timeout'].apply(
            lambda x: x == pd.Timestamp(year=x.year, month=x.month, day=x.day, hour=timeout_hour,
                                        minute=timeout_minute))
        self.df['is_late_out'] = self.df['timeout'].apply(
            lambda x: x > pd.Timestamp(year=x.year, month=x.month, day=x.day, hour=timeout_hour, minute=timeout_minute))

        return self.df
