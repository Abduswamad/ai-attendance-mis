from data_processors.timein_timeout_processing import TimeinTimeoutDataPreprocessor


def main():
    # Sample Data
    timein_timeout_data = {
        "first_name": ["ALi"],
        "timein": ["2024-05-18 09:05:00"],
        "timeout": ["2024-05-18 16:50:00"],
        "timein_status": ["LATE"],
        "timeout_status": ["EARLY OUT"]
    }
    # Data Preprocessing
    timein_timeout_preprocessor = TimeinTimeoutDataPreprocessor(timein_timeout_data)
    timein_timeout_data_frame = timein_timeout_preprocessor.clean_data()
    print(timein_timeout_data_frame)
    print(timein_timeout_data_frame.to_json(orient='records', date_format='iso'))

if __name__ == "__main__":
    main()
