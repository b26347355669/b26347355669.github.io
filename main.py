import cv2
import numpy as np
from matplotlib import pyplot as plt

map_img = cv2.imread('map3.png', 0)
incomplete_img = cv2.imread('incomplete.png', 0)

result = cv2.matchTemplate(map_img, incomplete_img, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + incomplete_img.shape[1],
                top_left[1] + incomplete_img.shape[0])
matched_img = map_img.copy()
cv2.rectangle(matched_img, top_left, bottom_right, 255, 2)

plt.imshow(matched_img, cmap='gray')
plt.title('Matched Location')
plt.show()
