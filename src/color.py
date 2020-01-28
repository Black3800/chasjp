import cv2


def whole_average_color(file_path):
    ### read file ###
    img = cv2.imread(file_path, 1)
    size = img.shape[0]

    ### compute ###
    b, g, r = 0, 0, 0
    for i in range(size):
        for j in range(size):
            b += img[i][j][0]
            g += img[i][j][1]
            r += img[i][j][2]

    b /= size*size
    g /= size*size
    r /= size*size
    return [int(round(b)), int(round(g)), int(round(r))]


def side_average_color(file_path):
    ### read file ###
    img = cv2.imread(file_path, 1)
    size = img.shape[0]

    ### compute ###
    top = img[0, :]
    bottom = img[-1, :]
    left = img[:, 0]
    right = img[:, -1]
    colors = []

    b, g, r = 0, 0, 0
    for i in range(size):
        b += top[i][0]
        g += top[i][1]
        r += top[i][2]
    b /= size
    g /= size
    r /= size
    colors.append([int(round(b)), int(round(g)), int(round(r))])

    b, g, r = 0, 0, 0
    for i in range(size):
        b += bottom[i][0]
        g += bottom[i][1]
        r += bottom[i][2]
    b /= size
    g /= size
    r /= size
    colors.append([int(round(b)), int(round(g)), int(round(r))])

    b, g, r = 0, 0, 0
    for i in range(size):
        b += left[i][0]
        g += left[i][1]
        r += left[i][2]
    b /= size
    g /= size
    r /= size
    colors.append([int(round(b)), int(round(g)), int(round(r))])

    b, g, r = 0, 0, 0
    for i in range(size):
        b += right[i][0]
        g += right[i][1]
        r += right[i][2]
    b /= size
    g /= size
    r /= size
    colors.append([int(round(b)), int(round(g)), int(round(r))])

    return colors
