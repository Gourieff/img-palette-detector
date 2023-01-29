import cv2
import numpy as np

def dominant_color(image, k=5):
    # reshape the image to be a 2D array of pixels and 3 color values (RGB)
    pixels = np.float32(image).reshape((-1, 3))

    # perform k-means clustering on the pixel colors
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, labels, palette = cv2.kmeans(pixels, k, None, criteria, 10, flags)

    # convert the palette (colors) back to 8-bit integers
    palette = np.uint8(palette)

    return palette