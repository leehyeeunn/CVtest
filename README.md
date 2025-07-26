1. 크기 조정(resize) -> cv.resize() 이용해서 224x224 크기로 재조정
2. 색상 변환 -> cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 이용해서 BGR에서 GRAY로 바꾸었다
3. 정규화 -> 픽셀 값을 255로 나누어서 0에서 1로 범위 조정
4. 노이즈 제거(blur) -> cv2.GaussianBlur() 이용해서 처리
5. 좌우 반전 -> cv2.flip 이용
6. 회전 -> 행렬을 생성하여 회전 변환을 적용
7. 색상 변화 -> 이번엔 무채색 말고 다른 색으로 일부 변경
