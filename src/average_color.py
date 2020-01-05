import cv2


def average_color(file_path):
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
