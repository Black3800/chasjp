import math
from src.average_color import *
from src.glcm import get_glcm_all_props

class Piece:

    def __init__(self, img, n):
        self.img_path = "cropped/" + img + "/" + img + "_crop" + str(n) + ".png"
        self.average_color = average_color(self.img_path)
        # self.glcm = get_glcm_all_props(self.img_path)
        self.top = -1
        self.bottom = -1
        self.left = -1
        self.right = -1

        print(self.img_path)
        print(self.average_color)
        # print(self.glcm)


def h(a, b):

    average_color_distance = math.sqrt((b.average_color[0] - a.average_color[0])**2 + (b.average_color[1] - a.average_color[1])**2 + (b.average_color[2] - a.average_color[2])**2)
    return average_color_distance


puzzle = []
for i in range(0, 5):
    puzzle.append(Piece("autumn", i))

print(puzzle)
# first = Piece("autumn", 1)
# second = Piece("autumn", 23)
# h(first, second)

for i in range(0, 5):
    for j in range(i+1, 5):
        print(str(i), "<->", str(j), h(puzzle[i], puzzle[j]))
