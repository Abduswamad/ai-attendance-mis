from data_processors.timein_timeout_processing import TimeinTimeoutDataPreprocessor


def main():
    # Sample Data
    timein_timeout_data = [
        {"Id Number":"01","timein":"2023-01-02 08:47:00","timeout":"2023-01-02 09:00:00"},
        {"Id Number":"01","timein":"2023-01-03 08:03:00","timeout":"2023-01-03 17:02:00"},
        {"Id Number":"01","timein":"2023-01-04 09:39:00","timeout":"2023-01-04 17:48:00"},
        {"Id Number":"01","timein":"2023-01-05 09:21:00","timeout":"2023-01-05 18:11:00"},
        {"Id Number":"01","timein":"2023-01-06 08:23:00","timeout":"2023-01-06 16:29:00"},
        {"Id Number":"02","timein":"2023-01-02 09:05:00","timeout":"2023-01-02 18:02:00"},
        {"Id Number":"02","timein":"2023-01-03 08:45:00","timeout":"2023-01-03 17:41:00"},
        {"Id Number":"02","timein":"2023-01-04 09:12:00","timeout":"2023-01-04 18:05:00"},
        {"Id Number":"02","timein":"2023-01-05 08:34:00","timeout":"2023-01-05 17:10:00"},
        {"Id Number":"02","timein":"2023-01-06 09:07:00","timeout":"2023-01-06 17:56:00"},
        {"Id Number":"03","timein":"2023-01-02 08:21:00","timeout":"2023-01-02 16:59:00"},
        {"Id Number":"03","timein":"2023-01-03 08:52:00","timeout":"2023-01-03 17:40:00"},
        {"Id Number":"03","timein":"2023-01-04 08:39:00","timeout":"2023-01-04 17:42:00"},
        {"Id Number":"03","timein":"2023-01-05 09:05:00","timeout":"2023-01-05 18:01:00"},
        {"Id Number":"03","timein":"2023-01-06 08:32:00","timeout":"2023-01-06 16:59:00"},
        {"Id Number":"04","timein":"2023-01-02 09:11:00","timeout":"2023-01-02 18:04:00"},
        {"Id Number":"04","timein":"2023-01-03 09:01:00","timeout":"2023-01-03 18:00:00"},
        {"Id Number":"04","timein":"2023-01-04 08:34:00","timeout":"2023-01-04 17:38:00"},
        {"Id Number":"04","timein":"2023-01-05 08:53:00","timeout":"2023-01-05 17:51:00"},
        {"Id Number":"04","timein":"2023-01-06 08:50:00","timeout":"2023-01-06 17:55:00"},
        {"Id Number":"05","timein":"2023-01-02 09:22:00","timeout":"2023-01-02 18:15:00"},
        {"Id Number":"05","timein":"2023-01-03 08:40:00","timeout":"2023-01-03 17:20:00"},
        {"Id Number":"05","timein":"2023-01-04 09:19:00","timeout":"2023-01-04 18:02:00"},
        {"Id Number":"05","timein":"2023-01-05 08:41:00","timeout":"2023-01-05 17:34:00"},
        {"Id Number":"05","timein":"2023-01-06 09:04:00","timeout":"2023-01-06 17:55:00"},
        {"Id Number":"06","timein":"2023-01-02 09:00:00","timeout":"2023-01-02 17:45:00"},
        {"Id Number":"06","timein":"2023-01-03 08:30:00","timeout":"2023-01-03 17:20:00"},
        {"Id Number":"06","timein":"2023-01-04 09:10:00","timeout":"2023-01-04 18:00:00"},
        {"Id Number":"06","timein":"2023-01-05 08:45:00","timeout":"2023-01-05 17:35:00"},
        {"Id Number":"06","timein":"2023-01-06 09:20:00","timeout":"2023-01-06 18:05:00"},
        {"Id Number":"07","timein":"2023-01-02 08:30:00","timeout":"2023-01-02 17:10:00"},
        {"Id Number":"07","timein":"2023-01-03 08:40:00","timeout":"2023-01-03 17:30:00"},
        {"Id Number":"07","timein":"2023-01-04 09:00:00","timeout":"2023-01-04 18:00:00"},
        {"Id Number":"07","timein":"2023-01-05 08:45:00","timeout":"2023-01-05 17:40:00"},
        {"Id Number":"07","timein":"2023-01-06 09:10:00","timeout":"2023-01-06 17:55:00"},
        {"Id Number":"08","timein":"2023-01-02 09:05:00","timeout":"2023-01-02 18:00:00"},
        {"Id Number":"08","timein":"2023-01-03 08:45:00","timeout":"2023-01-03 17:35:00"},
        {"Id Number":"08","timein":"2023-01-04 09:15:00","timeout":"2023-01-04 18:10:00"},
        {"Id Number":"08","timein":"2023-01-05 08:35:00","timeout":"2023-01-05 17:20:00"},
        {"Id Number":"08","timein":"2023-01-06 09:10:00","timeout":"2023-01-06 17:55:00"},
        {"Id Number":"09","timein":"2023-01-02 08:50:00","timeout":"2023-01-02 17:40:00"},
        {"Id Number":"09","timein":"2023-01-03 08:40:00","timeout":"2023-01-03 17:30:00"},
        {"Id Number":"09","timein":"2023-01-04 09:00:00","timeout":"2023-01-04 17:55:00"},
        {"Id Number":"09","timein":"2023-01-05 08:45:00","timeout":"2023-01-05 17:35:00"},
        {"Id Number":"09","timein":"2023-01-06 09:10:00","timeout":"2023-01-06 17:55:00"},
        {"Id Number":"10","timein":"2023-01-02 09:05:00","timeout":"2023-01-02 18:00:00"},
        {"Id Number":"10","timein":"2023-01-03 08:45:00","timeout":"2023-01-03 17:35:00"},
        {"Id Number":"10","timein":"2023-01-04 09:15:00","timeout":"2023-01-04 18:10:00"},
        {"Id Number":"10","timein":"2023-01-05 08:35:00","timeout":"2023-01-05 17:20:00"},
        {"Id Number":"10","timein":"2023-01-06 09:10:00","timeout":"2023-01-06 17:55:00"},
        {"Id Number":"11","timein":"2023-01-02 09:05:00","timeout":"2023-01-02 18:00:00"},
        {"Id Number":"11","timein":"2023-01-03 08:45:00","timeout":"2023-01-03 17:35:00"},
        {"Id Number":"11","timein":"2023-01-04 09:15:00","timeout":"2023-01-04 18:10:00"},
    ]
    # Data Preprocessing
    timein_timeout_preprocessor = TimeinTimeoutDataPreprocessor(timein_timeout_data)
    timein_timeout_data_frame = timein_timeout_preprocessor.clean_data()
    print(timein_timeout_data_frame.to_json(orient='records', date_format='iso'))

if __name__ == "__main__":
    main()




