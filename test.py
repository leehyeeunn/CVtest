import numpy as np
import cv2
def generate_depth_map(image):
    if image is None:
        raise ValueError("입력된 이미지가 없습니다.")
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    depth_map = cv2.applyColorMap(grayscale, cv2.COLORMAP_JET)
    return depth_map

def test_generate_depth_map():
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    depth_map = generate_depth_map(image)

    assert depth_map.shape == image.shape, "출력 크기가 입력과 다릅니다."
    assert isinstance(depth_map, np.ndarray), "출력이 ndarray가 아닙니다."
