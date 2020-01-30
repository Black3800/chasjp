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
    whole_color_diff_value = 10 - color_diff[0] * 0.03921568627451
    texture_diff = get_glcm_difference(a, b)
    texture_diff_value = (10 - texture_diff[0] * 0.5) + (10 - texture_diff[1] * 0.5) + (10 - texture_diff[2] * 0.5) + \
                         (10 - texture_diff[3] * 0.5) + (10 - texture_diff[4] * 0.5) + (10 - texture_diff[5] * 0.5)
    # result.append(color_diff[0]*10/255 + color_diff[1]*30/255)
    if not is_edge_match(a.top, b.bottom):
        result.append(0)
    else:
        result.append(whole_color_diff_value + (30 - color_diff[1] * 0.11764705882353) + texture_diff_value)

    if not is_edge_match(a.bottom, b.top):
        result.append(0)
    else:
        result.append(whole_color_diff_value + (30 - color_diff[2] * 0.11764705882353) + texture_diff_value)

    if not is_edge_match(a.left, b.right):
        result.append(0)
    else:
        result.append(whole_color_diff_value + (30 - color_diff[3] * 0.11764705882353) + texture_diff_value)

    if not is_edge_match(a.right, b.left):
        result.append(0)
    else:
        result.append(whole_color_diff_value + (30 - color_diff[4] * 0.11764705882353) + texture_diff_value)
    return result


def check_status(status):
    size = len(status)
    final = 0
    count = 0
    if size == 2:
        final = 4
    else:
        final = 2 * size * (size-1)
    for ex in status:
        for ey in ex:
            if ey[0] != -1:
                count += 1
    return count == 2 * final


def reveal_solution(status):
    size = len(status)
    for i in range(size):
        for j in range(4):
            if status[i][j] != 0:
                # print(i, "<->", status[i][j], " (", j, ")")
                if j == 0:
                    print(i, "'s top is ", status[i][j][1])
                elif j == 1:
                    print(i, "'s bottom is ", status[i][j][1])
                elif j == 2:
                    print(i, "'s left is ", status[i][j][1])
                elif j == 3:
                    print(i, "'s right is ", status[i][j][1])


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

# htable = []
# for xx in range(25):
#     wtf = []
#     for yy in range(25):
#         wtf.append([])
#     htable.append(wtf)

hlist = []

# for i in range(0, 20):
#     print(heuristic(Piece("student", i), Piece("student", i+5))[3])

print("Processing...")
for i in range(0, 25):
    piece_a = Piece("student", i)
    for j in range(i, 25):
        if i == j:
            continue
        piece_b = Piece("student", j)
        hf = heuristic(piece_a, piece_b)
        # htable[i][j] = heuristic(piece_a, piece_b)
        for hv in hf:
            mytuple = (hv, i, j, hf.index(hv))
            hlist.append(mytuple)


hlist = sorted(hlist, key=lambda x: x[0], reverse=True)
print(hlist)

status = [[(-1, -1), (-1, -1), (-1, -1), (-1, -1)] for kk in range(25)]
calculated = 0

for x in hlist:
    if check_status(status):
        break
    i = 0
    j = 0
    if x[3] == 0:
        i = 0
        j = 1
    elif x[3] == 1:
        i = 1
        j = 0
    elif x[3] == 2:
        i = 2
        j = 3
    elif x[3] == 3:
        i = 3
        j = 2

    if x[0] > status[x[1]][i][0]:
        if status[x[1]][i][1] != -1:
            calculated -= 1
            status[status[x[1]][i][1]][i] = (-1, -1)
        calculated += 1
        status[x[1]][i] = (x[0], x[2])
        status[x[2]][j] = (x[0], x[1])
        print(calculated)

print(check_status(status))
print(hlist)
print(status)
reveal_solution(status)
