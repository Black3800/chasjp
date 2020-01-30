import cv2


def get_left_edge(file_path):
    img = cv2.imread(file_path, 0)
    size = img.shape[0]
    sigma = int(size * 0.028)
    img = cv2.bilateralFilter(img, 10, sigma, sigma)
    img = cv2.bilateralFilter(img, 20, sigma, sigma)
    left_col = img[:, 0]
    difference = []
    edges = []

    for i in range(0, size - 1):
        change = int(left_col[i + 1]) - int(left_col[i])
        difference.append(change)
        if change > 40:
            edges.append(i)

    return edges


def get_right_edge(file_path):
    img = cv2.imread(file_path, 0)
    size = img.shape[0]
    sigma = int(size * 0.028)
    img = cv2.bilateralFilter(img, 10, sigma, sigma)
    img = cv2.bilateralFilter(img, 20, sigma, sigma)
    right_col = img[:, -1]
    difference = []
    edges = []

    for i in range(0, size - 1):
        change = int(right_col[i + 1]) - int(right_col[i])
        difference.append(change)
        if change > 40:
            edges.append(i)

    return edges


def get_top_edge(file_path):
    img = cv2.imread(file_path, 0)
    size = img.shape[0]
    sigma = int(size * 0.028)
    img = cv2.bilateralFilter(img, 10, sigma, sigma)
    img = cv2.bilateralFilter(img, 20, sigma, sigma)
    top_col = img[0, :]
    difference = []
    edges = []

    for i in range(0, size - 1):
        change = int(top_col[i + 1]) - int(top_col[i])
        difference.append(change)
        if change > 40:
            edges.append(i)

    return edges


def get_bottom_edge(file_path):
    img = cv2.imread(file_path, 0)
    size = img.shape[0]
    sigma = int(size * 0.028)
    img = cv2.bilateralFilter(img, 10, sigma, sigma)
    img = cv2.bilateralFilter(img, 20, sigma, sigma)
    bottom_col = img[-1, :]
    difference = []
    edges = []

    for i in range(0, size - 1):
        change = int(bottom_col[i + 1]) - int(bottom_col[i])
        difference.append(change)
        if change > 40:
            edges.append(i)

    return edges


def clean_edge(edge):
    # merge edges that differ by 1
    # delList = []
    i = 0
    while i < (len(edge) - 1):
        if abs(edge[i] - edge[i + 1]) == 1:
            del edge[i]
            i -= 1
        i += 1

    # for x in range(-1, -1*len(delList) - 1, -1):
    #     del edge[x+i+1]
    return edge


def is_edge_match(edges1, edges2, fault = 0, penalty = 0):
    # Array subset problem:
    # O(m log m + n log n)
    # m = len(edges1)
    # n = len(edges2)
    len_edges1 = len(edges1)
    len_edges2 = len(edges2)
    threshold = 2
    if len_edges1 + len_edges2 == 0:
        return True
    elif len_edges1 > 0 and len_edges2 > 0:
        if len_edges1 == len_edges2:
            for i in range(0, len_edges1):
                if abs(edges1[i] - edges2[i]) > threshold:
                    # print("↓-- ", edges1[i], " != ", edges2[i])
                    fault += 1
                    penalty += 1
                    if edges1[i] < edges2[i]:
                        del edges1[i]
                    else:
                        del edges2[i]
                    return is_edge_match(edges1, edges2, fault, penalty)
            return True
        else:
            larger = edges1
            smaller = edges1
            if len_edges1 > len_edges2:
                smaller = edges2
            else:
                larger = edges2
            maximum = len(larger)
            minimum = len(smaller)

            i = 0
            j = 0
            # print(i, j)
            while i < maximum and j < minimum:
                # print(i)
                if abs(larger[i] - smaller[j]) <= threshold:
                    i += 1
                    j += 1
                elif larger[i] < smaller[j]:
                    i += 1
                elif larger[i] > smaller[j]:
                    # print("↓-- ", larger[i], " > ", smaller[j])
                    j += 1
                    fault += 1
                    if fault/(minimum + penalty) > 0.2:
                        # print("↓-- ", fault/(minimum + penalty), ", fault over 0.2, return false")
                        return False
                    # return False
            return not (j < minimum)
    # return True if > 80%
    return False


# get_left_most("cropped/student/student_crop12.png", "cropped/student/student_crop13.png")
# print(get_left_edge("cropped/student/student_crop13.png"))
# print(get_right_edge("cropped/student/student_crop12.png"))
# print(get_top_edge("cropped/student/student_crop21.png"))
# print(get_bottom_edge("cropped/student/student_crop16.png"))

# print(is_edge_match(get_left_edge("cropped/student/student_crop13.png"),
#                     get_right_edge("cropped/student/student_crop12.png")))
# print(is_edge_match(get_top_edge("cropped/student/student_crop21.png"),
#                     get_bottom_edge("cropped/student/student_crop16.png")))
# print(is_edge_match(get_right_edge("cropped/lighthouse/lighthouse_crop14.png"),
#                     get_left_edge("cropped/lighthouse/lighthouse_crop15.png")))
# print(is_edge_match(get_bottom_edge("cropped/cliff/cliff_crop19.png"),
#                     get_top_edge("cropped/cliff/cliff_crop26.png")))
# print(get_top_edge("cropped/cliff/cliff_crop26.png"))
# print(get_bottom_edge("cropped/cliff/cliff_crop19.png"))
# print(clean_edge(get_top_edge("cropped/cliff/cliff_crop26.png")))
# print(clean_edge(get_bottom_edge("cropped/cliff/cliff_crop19.png")))

# alpha = [1, 6, 9, 16, 18, 21, 25, 26]
# beta = [1, 4, 9, 15, 18, 22]
# print(alpha)
# print(beta)
# print(is_edge_match(alpha, beta))

# fix this!!!
