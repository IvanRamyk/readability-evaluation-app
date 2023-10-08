from joblib import load


class ReadabilityEvaluationModel:
    MODEL_PATH = "pipelines/readability_prediction_pipeline_v1.joblib"

    def __init__(self):
        self.model = None

    def _load_model(self):
        self.model = load(ReadabilityEvaluationModel.MODEL_PATH)

    def predict(self, text) -> float:
        if self.model is None:
            self._load_model()
        [prediction] = self.model.predict([text])
        return prediction
