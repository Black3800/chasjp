import cv2
from src.edge import *


def f(x, y):
    return (x*y) % 2 == 0


img = "lighthouse"
result = []
size = 8
count = size * (size - 1)
for i in range(0, count):
    # first = (i % size) + (int(i/size)*size*2)
    # second = first + size
    first = i
    second = first + size
    img_path_first = "cropped/" + img + "/" + img + "_crop" + str(first) + ".png"
    img_path_second = "cropped/" + img + "/" + img + "_crop" + str(second) + ".png"
    # print(img_path_first)
    # print(img_path_second)
    img_first = get_bottom_edge(img_path_first)
    img_second = get_top_edge(img_path_second)
    # print(first, second)
    res = is_edge_match(clean_edge(img_first), clean_edge(img_second))
    if not res:
        print(i, img_first, img_second, "\n")
    result.append(res)


print(result)

# print(is_edge_match([200, 222, 303, 321, 333, 339, 345], [200, 222, 281, 302, 321, 333]))
alpha = [1, 6, 9, 16, 18, 21, 25, 26]
beta = [1, 4, 9, 15, 18, 22]
print(alpha)
print(beta)
print(is_edge_match(alpha, beta))