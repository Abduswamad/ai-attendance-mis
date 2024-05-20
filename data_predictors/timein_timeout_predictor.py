
class TimeinTimeoutPredictor:
    def __init__(self, model):
        self.model = model

    def predict_attendance(self, new_data):
        if self.model is None:
            raise Exception("Model is not trained. Please train the model before making predictions.")

        return self.model.predict(new_data)
