# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:47:52 2023

@author: asus
"""

import cv2
import numpy as np

demo = cv2.imread("D:/.smt3/SKD/RSA/test.png", 0)
r, c = demo.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)
cv2.imwrite("D:/.smt3/SKD/RSA/KEY-test.png", key)

cv2.imshow("demo", demo)
cv2.imshow("key", key)

encryption = cv2.bitwise_xor(demo, key)
cv2.imwrite("D:/.smt3/SKD/RSA/ENC-test.png", encryption)
decryption = cv2.bitwise_xor(encryption, key)
cv2.imwrite("D:/.smt3/SKD/RSA/DEC-test.png", decryption)

cv2.imshow("encryption", encryption)
cv2.imshow("decryption", decryption)

cv2.waitKey(-1)
cv2.destroyAllWindows()