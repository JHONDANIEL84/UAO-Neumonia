import numpy as np
import pytest

@pytest.fixture
def dummy_img_array():
    # Imagen falsa tipo (H, W, C)
    return np.zeros((250, 250, 3), dtype=np.uint8)

@pytest.fixture
def dummy_batch(dummy_img_array):
    # Batch tipo (1, H, W, C)
    return np.expand_dims(dummy_img_array, axis=0)
