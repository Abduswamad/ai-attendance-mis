from data_processors.timein_timeout_processor import TimeInTimeOutDataProcessor
from data_analysers.timein_timeout_analysor import TimeInTimeOutDataAnalyzer
from data_trainers.timein_timeout_trainer import TimeInTimeOutTrainer
import pandas as pd


def main():
    # Sample Data
    # Example usage:
    # time_in_time_out_data = pd.read_csv('attendance_data.csv')
    time_in_time_out_data = [
        {"Id Number":"01","time_in":"2023-01-02 08:47:00","time_out":"2023-01-02 09:00:00"},
        {"Id Number":"01","time_in":"2023-01-03 08:03:00","time_out":"2023-01-03 17:02:00"},
        {"Id Number":"01","time_in":"2023-01-04 09:39:00","time_out":"2023-01-04 17:48:00"},
        {"Id Number":"01","time_in":"2023-01-05 09:21:00","time_out":"2023-01-05 18:11:00"},
        {"Id Number":"01","time_in":"2023-01-06 08:23:00","time_out":"2023-01-06 16:29:00"},
        {"Id Number":"02","time_in":"2023-01-02 09:05:00","time_out":"2023-01-02 18:02:00"},
        {"Id Number":"02","time_in":"2023-01-03 08:45:00","time_out":"2023-01-03 17:41:00"},
        {"Id Number":"02","time_in":"2023-01-04 09:12:00","time_out":"2023-01-04 18:05:00"},
        {"Id Number":"02","time_in":"2023-01-05 08:34:00","time_out":"2023-01-05 17:10:00"},
        {"Id Number":"02","time_in":"2023-01-06 09:07:00","time_out":"2023-01-06 17:56:00"},
        {"Id Number":"03","time_in":"2023-01-02 08:21:00","time_out":"2023-01-02 16:59:00"},
        {"Id Number":"03","time_in":"2023-01-03 08:52:00","time_out":"2023-01-03 17:40:00"},
        {"Id Number":"03","time_in":"2023-01-04 08:39:00","time_out":"2023-01-04 17:42:00"},
        {"Id Number":"03","time_in":"2023-01-05 09:05:00","time_out":"2023-01-05 18:01:00"},
        {"Id Number":"03","time_in":"2023-01-06 08:32:00","time_out":"2023-01-06 16:59:00"},
        {"Id Number":"04","time_in":"2023-01-02 09:11:00","time_out":"2023-01-02 18:04:00"},
        {"Id Number":"04","time_in":"2023-01-03 09:01:00","time_out":"2023-01-03 18:00:00"},
        {"Id Number":"04","time_in":"2023-01-04 08:34:00","time_out":"2023-01-04 17:38:00"},
        {"Id Number":"04","time_in":"2023-01-05 08:53:00","time_out":"2023-01-05 17:51:00"},
        {"Id Number":"04","time_in":"2023-01-06 08:50:00","time_out":"2023-01-06 17:55:00"},
        {"Id Number":"05","time_in":"2023-01-02 09:22:00","time_out":"2023-01-02 18:15:00"},
        {"Id Number":"05","time_in":"2023-01-03 08:40:00","time_out":"2023-01-03 17:20:00"},
        {"Id Number":"05","time_in":"2023-01-04 09:19:00","time_out":"2023-01-04 18:02:00"},
        {"Id Number":"05","time_in":"2023-01-05 08:41:00","time_out":"2023-01-05 17:34:00"},
        {"Id Number":"05","time_in":"2023-01-06 09:04:00","time_out":"2023-01-06 17:55:00"},
        {"Id Number":"06","time_in":"2023-01-02 09:00:00","time_out":"2023-01-02 17:45:00"},
        {"Id Number":"06","time_in":"2023-01-03 08:30:00","time_out":"2023-01-03 17:20:00"},
        {"Id Number":"06","time_in":"2023-01-04 09:10:00","time_out":"2023-01-04 18:00:00"},
        {"Id Number":"06","time_in":"2023-01-05 08:45:00","time_out":"2023-01-05 17:35:00"},
        {"Id Number":"06","time_in":"2023-01-06 09:20:00","time_out":"2023-01-06 18:05:00"},
        {"Id Number":"07","time_in":"2023-01-02 08:30:00","time_out":"2023-01-02 17:10:00"},
        {"Id Number":"07","time_in":"2023-01-03 08:40:00","time_out":"2023-01-03 17:30:00"},
        {"Id Number":"07","time_in":"2023-01-04 09:00:00","time_out":"2023-01-04 18:00:00"},
        {"Id Number":"07","time_in":"2023-01-05 08:45:00","time_out":"2023-01-05 17:40:00"},
        {"Id Number":"07","time_in":"2023-01-06 09:10:00","time_out":"2023-01-06 17:55:00"},
        {"Id Number":"08","time_in":"2023-01-02 09:05:00","time_out":"2023-01-02 18:00:00"},
        {"Id Number":"08","time_in":"2023-01-03 08:45:00","time_out":"2023-01-03 17:35:00"},
        {"Id Number":"08","time_in":"2023-01-04 09:15:00","time_out":"2023-01-04 18:10:00"},
        {"Id Number":"08","time_in":"2023-01-05 08:35:00","time_out":"2023-01-05 17:20:00"},
        {"Id Number":"08","time_in":"2023-01-06 09:10:00","time_out":"2023-01-06 17:55:00"},
        {"Id Number":"09","time_in":"2023-01-02 08:50:00","time_out":"2023-01-02 17:40:00"},
        {"Id Number":"09","time_in":"2023-01-03 08:40:00","time_out":"2023-01-03 17:30:00"},
        {"Id Number":"09","time_in":"2023-01-04 09:00:00","time_out":"2023-01-04 17:55:00"},
        {"Id Number":"09","time_in":"2023-01-05 08:45:00","time_out":"2023-01-05 17:35:00"},
        {"Id Number":"09","time_in":"2023-01-06 09:10:00","time_out":"2023-01-06 17:55:00"},
        {"Id Number":"10","time_in":"2023-01-02 09:05:00","time_out":"2023-01-02 18:00:00"},
        {"Id Number":"10","time_in":"2023-01-03 08:45:00","time_out":"2023-01-03 17:35:00"},
        {"Id Number":"10","time_in":"2023-01-04 09:15:00","time_out":"2023-01-04 18:10:00"},
        {"Id Number":"10","time_in":"2023-01-05 08:35:00","time_out":"2023-01-05 17:20:00"},
        {"Id Number":"10","time_in":"2023-01-06 09:10:00","time_out":"2023-01-06 17:55:00"},
        {"Id Number":"11","time_in":"2023-01-02 09:05:00","time_out":"2023-01-02 18:00:00"},
        {"Id Number":"11","time_in":"2023-01-03 08:45:00","time_out":"2023-01-03 17:35:00"},
        {"Id Number":"11","time_in":"2023-01-04 09:15:00","time_out":"2023-01-04 18:10:00"},
    ]
    # Data Preprocessing
    time_in_time_out_preprocessor = TimeInTimeOutDataProcessor(time_in_time_out_data)
    time_in_time_out_processed_data = time_in_time_out_preprocessor.process_data()


    # Data Analysis
    time_in_time_out_analyzer = TimeInTimeOutDataAnalyzer(time_in_time_out_processed_data)
    time_in_time_out_summary = time_in_time_out_analyzer.summarize_data()
    time_in_time_out_analysed_data = time_in_time_out_analyzer.feature_engineering()


    # Data trainer
    time_in_time_out_trainer = TimeInTimeOutTrainer(time_in_time_out_analysed_data)
    time_in_time_out_trainer.train_model()
    predicted_id = time_in_time_out_trainer.predict_id("2023-01-04 08:00:00", "2023-01-04 17:00:00")
    print("Summary Statistics: ", time_in_time_out_summary)
    print(f"The predicted Id Number is: {predicted_id}")


if __name__ == "__main__":
    main()




