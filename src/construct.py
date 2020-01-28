import math
from src.color import *
from src.glcm import get_glcm_all_props
from src.edge import *
import numpy

class Piece:

    def __init__(self, img, n):
        self.img_path = "cropped/" + img + "/" + img + "_crop" + str(n) + ".png"
        self.n = n
        self.average_color = [whole_average_color(self.img_path), *side_average_color(self.img_path)]
        # self.average_color = [0, 0, 0]

        glcm = get_glcm_all_props(self.img_path)
        self.contrast = numpy.sum(glcm["contrast"])
        self.dissimilarity = numpy.sum(glcm["dissimilarity"])
        self.homogeneity = numpy.sum(glcm["homogeneity"])
        self.asm = numpy.sum(glcm["asm"])
        self.energy = numpy.sum(glcm["energy"])
        self.correlation = numpy.sum(glcm["correlation"])
        del glcm

        self.top = get_top_edge(self.img_path)
        self.bottom = get_bottom_edge(self.img_path)
        self.left = get_left_edge(self.img_path)
        self.right = get_right_edge(self.img_path)

        # print(self.img_path)
        # print(self.average_color)


def get_color_difference(a, b):

    difference = [math.sqrt((b.average_color[0][0] - a.average_color[0][0]) ** 2 +
                            (b.average_color[0][1] - a.average_color[0][1]) ** 2 +
                            (b.average_color[0][2] - a.average_color[0][2]) ** 2),
                  math.sqrt((b.average_color[2][0] - a.average_color[1][0]) ** 2 +
                            (b.average_color[2][1] - a.average_color[1][1]) ** 2 +
                            (b.average_color[2][2] - a.average_color[1][2]) ** 2),
                  math.sqrt((b.average_color[1][0] - a.average_color[2][0]) ** 2 +
                            (b.average_color[1][1] - a.average_color[2][1]) ** 2 +
                            (b.average_color[1][2] - a.average_color[2][2]) ** 2),
                  math.sqrt((b.average_color[4][0] - a.average_color[3][0]) ** 2 +
                            (b.average_color[4][1] - a.average_color[3][1]) ** 2 +
                            (b.average_color[4][2] - a.average_color[3][2]) ** 2),
                  math.sqrt((b.average_color[3][0] - a.average_color[4][0]) ** 2 +
                            (b.average_color[3][1] - a.average_color[4][1]) ** 2 +
                            (b.average_color[3][2] - a.average_color[4][2]) ** 2)]

    # difference = [ whole,
    #                a.top to b.bottom,
    #                a.bottom to b.top,
    #                a.left to b.right,
    #                a.right to b.left, ]

    return difference


def get_glcm_difference(a, b):

    # print(str(numpy.sum(a.glcm["contrast"])), str(numpy.sum(b.glcm["contrast"])))
    difference = [abs(b.contrast - a.contrast),
                  abs(b.dissimilarity - a.dissimilarity),
                  abs(b.homogeneity - a.homogeneity),
                  abs(b.asm - a.asm),
                  abs(b.energy - a.energy),
                  abs(b.correlation - a.correlation)]
    return difference


def heuristic(a, b):
    result = []
    color_diff = get_color_difference(a, b)
    texture_diff = get_glcm_difference(a, b)
    # result.append(color_diff[0]*10/255 + color_diff[1]*30/255)

    if not is_edge_match(a.bottom, b.top):
        return 0
    result.append((10 - color_diff[0] * 0.03921568627451) + (30 - color_diff[1] * 0.11764705882353) +
                  (10 - texture_diff[0] * 0.5) + (10 - texture_diff[1] * 0.5) + (10 - texture_diff[2] * 0.5) +
                  (10 - texture_diff[3] * 0.5) + (10 - texture_diff[4] * 0.5) + (10 - texture_diff[5] * 0.5))
    return result


puzzle = []
# for i in range(37, 42):
#     puzzle.append(Piece("cliff", i))

# print(puzzle)
# first = Piece("student", 4)
# second = Piece("student", 9)
# print(heuristic(first, second))

# for i in range(0, 5):
#     for j in range(i+1, 5):
#         print(str(puzzle[i].n), "<->", str(puzzle[j].n), get_color_difference(puzzle[i], puzzle[j]))

# for i in range(0, 5):
#     for j in range(i+1, 5):
#         print(str(puzzle[i].n), "<->", str(puzzle[j].n), get_glcm_difference(puzzle[i], puzzle[j]))

for i in range(0, 20):
    print(heuristic(Piece("student", i), Piece("student", i+5)))
