import numpy as np
from detector_neumonia import predict

class DummyModel:
    def predict(self, x):
        return np.array([[0.1, 0.8, 0.1]])  # 3 clases

def test_predict_returns_expected_types(dummy_img_array, monkeypatch):
    # mock del modelo
    monkeypatch.setattr("detector_neumonia.model_fun", lambda: DummyModel())

    # mock del grad_cam (devuelve una imagen 250x250 tipo uint8)
    monkeypatch.setattr(
        "detector_neumonia.grad_cam",
        lambda array: np.zeros((250, 250, 3), dtype=np.uint8),
    )

    label, proba, heatmap = predict(dummy_img_array)

    assert isinstance(label, str)
    assert isinstance(proba, float)
    assert isinstance(heatmap, np.ndarray)
    assert heatmap.shape == (250, 250, 3)

import numpy as np
from detector_neumonia import preprocess


def test_preprocess_returns_batch(dummy_img_array):
    """
    Verifica que preprocess:
    - Retorne un numpy array
    - Tenga forma (1, H, W, C)
    - Use tipo float32
    """

    batch = preprocess(dummy_img_array)

    assert isinstance(batch, np.ndarray)
    assert batch.ndim == 4              # (1, H, W, C)
    assert batch.shape[0] == 1
    assert batch.dtype == np.float32
