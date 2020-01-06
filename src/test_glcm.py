"""

from src.glcm_old import horizontal_glcm, vertical_glcm, diagonal_glcm

g = horizontal_glcm("cropped/lighthouse/lighthouse_crop14.png")
h = vertical_glcm("cropped/lighthouse/lighthouse_crop14.png")
m = diagonal_glcm("cropped/lighthouse/lighthouse_crop14.png")

for i in range(10):
    s = ""
    for j in range(10):
        s += str(g[i][j]) + " "
    print(s)

print("---------------------------")

for i in range(10):
    s = ""
    for j in range(10):
        s += str(h[i][j]) + " "
    print(s)

print("---------------------------")

for i in range(10):
    s = ""
    for j in range(10):
        s += str(m[i][j]) + " "
    print(s)

"""

import json
from src.glcm import *

collected = []

for i in range(0, 36):
    collected.append(get_glcm_all_props("cropped/lighthouse/lighthouse_crop" + str(i) + ".png"))

file = open("cropped/lighthouse/lighthouse.json", "w")
file.write(json.dumps(collected))
file.close()

# Note:
# serializing numpy array
# https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable

# print(collected)
