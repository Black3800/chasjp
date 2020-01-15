import cv2


def get_left_most(file_path, file_path2):
    img = cv2.imread(file_path, 0)
    img2 = cv2.imread(file_path2, 0)
    # cv2.imshow("first", img)
    sigma = int(img.shape[0] * 0.028)
    img = cv2.bilateralFilter(img, 100, sigma, sigma)
    img2 = cv2.bilateralFilter(img2, 100, sigma, sigma)
    # gray_level_map = numpy.vectorize(get_gray_level_output)
    # leveled = numpy.array(gray_level_map(img), dtype=numpy.uint8)
    right = img[:, -1]
    left = img2[:, 0]
    diff = []
    diff2 = []
    second = [0]
    high = []
    high2 = []
    for i in range(0, img.shape[0]-1):

        # change = ((right[i + 1][0] - right[i][0])**2 + (right[i + 1][1] - right[i][1])**2 + (right[i + 1][2] - right[i][2])**2)
        # change2 = ((left[i + 1][0] - left[i][0])**2 + (left[i + 1][1] - left[i][1])**2 + (left[i + 1][2] - left[i][2])**2)
        change = int(right[i+1]) - int(right[i])
        change2 = int(left[i + 1]) - int(left[i])
        diff.append(change)
        diff2.append(change2)
        if change > 40:
            high.append(i)
        if change2 > 40:
            high2.append(i)

    # for i in range(0, len(diff)-1):
    #     second.append(int(diff[i+1]) - int(diff[i]))


    print(high)
    for x in high:
        print(x, diff[x], "->", diff[x+1])

    print("---")

    print(high2)
    for x in high2:
        print(x, diff2[x], "->", diff2[x+1])
    cv2.imshow("second", img)
    cv2.imshow("second2", img2)
    # plt.plot(diff, 'bo')
    # plt.plot(diff2, 'go')
    # plt.plot(second)
    # plt.ylabel("some nums")
    # plt.show()
    # cv2.imshow("leftonly", right)
    # print(diff)
    # print(diff2)
    cv2.waitKey()


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
    for i in range(0, len(edge) - 2):
        if abs(edge[i] - edge[i + 1]) == 1:
            # delList.append(i)
            del edge[i]
            i -= 1
    # for x in range(-1, -1*len(delList) - 1, -1):
    #     del edge[x+i+1]
    return edge


def is_edge_match(edges1, edges2):
    # Array subset problem:
    # O(m log m + n log n)
    # m = len(edges1)
    # n = len(edges2)
    edges1 = clean_edge(edges1)
    edges2 = clean_edge(edges2)
    len_edges1 = len(edges1)
    len_edges2 = len(edges2)
    if len_edges1 + len_edges2 == 0:
        return True
    elif len_edges1 > 0 and len_edges2 > 0:
        if len_edges1 == len_edges2:
            for i in range(0, len_edges1):
                if edges1[i] != edges2[i]:
                    return False
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
            while i < maximum and j < minimum:
                if abs(larger[i] - smaller[j]) <= 1:
                    i += 1
                    j += 1
                elif larger[i] < smaller[j]:
                    i += 1
                elif larger[i] > smaller[j]:
                    return False
            return not (j < minimum)
    return False


# get_left_most("cropped/student/student_crop12.png", "cropped/student/student_crop13.png")
# print(get_left_edge("cropped/student/student_crop13.png"))
# print(get_right_edge("cropped/student/student_crop12.png"))
# print(get_top_edge("cropped/student/student_crop21.png"))
# print(get_bottom_edge("cropped/student/student_crop16.png"))
print(is_edge_match(get_left_edge("cropped/student/student_crop13.png"),
                    get_right_edge("cropped/student/student_crop12.png")))
print(is_edge_match(get_top_edge("cropped/student/student_crop21.png"),
                    get_bottom_edge("cropped/student/student_crop16.png")))
print(is_edge_match(get_right_edge("cropped/lighthouse/lighthouse_crop14.png"),
                    get_left_edge("cropped/lighthouse/lighthouse_crop15.png")))
print(is_edge_match(get_bottom_edge("cropped/lighthouse/lighthouse_crop9.png"),
                    get_top_edge("cropped/lighthouse/lighthouse_crop15.png")))
print(get_top_edge("cropped/lighthouse/lighthouse_crop15.png"))
print(get_bottom_edge("cropped/lighthouse/lighthouse_crop9.png"))
print(clean_edge(get_top_edge("cropped/lighthouse/lighthouse_crop15.png")))
print(clean_edge(get_bottom_edge("cropped/lighthouse/lighthouse_crop9.png")))
# alpha = [1, 6, 9, 16, 18, 21, 25, 26]
# beta = [1, 4, 9, 15, 18, 22]
# print(alpha)
# print(beta)
# print(is_edge_match(alpha, beta))

# fix this!!!
