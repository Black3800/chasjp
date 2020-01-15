import cv2, numpy
from skimage.feature.texture import *


__GRAY_THRESHOLD = [0, 25, 50, 75, 100, 125, 151, 177, 203, 229, 256]


def get_gray_level(gray_val):
    arr = __GRAY_THRESHOLD
    l, r = 0, 10
    x = gray_val

    while l <= r:
        mid = int(l + (r - l) / 2)

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element was not present
    return r


def get_gray_level_output(gray_val):
    arr = __GRAY_THRESHOLD
    l, r = 0, 10
    x = gray_val

    while l <= r:
        mid = int(l + (r - l) / 2)

        # Check if x is present at mid
        if arr[mid] == x:
            return arr[mid]

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element was not present
    return arr[r]


def get_glcm_all_angle(file_path):
    ### return normalized glcm ###
    __DISTANCE = [1]
    __ANGLE = [0, numpy.pi/4, numpy.pi/2, numpy.pi*3/4, numpy.pi, numpy.pi*5/4, numpy.pi*3/2, numpy.pi*7/4]
    __LEVELS = 10

    img = cv2.imread(file_path, 0)
    gray_level_map = numpy.vectorize(get_gray_level)
    leveled = gray_level_map(img)
    glcm = greycomatrix(leveled, __DISTANCE, __ANGLE, levels=__LEVELS)
    all_angle = glcm[:, :, 0, :]
    summed = numpy.add(all_angle[0], all_angle[1])

    for i in range(2, __LEVELS):
        summed = numpy.add(summed, all_angle[i])

    final = summed/numpy.sum(summed)
    return final


def get_glcm_contrast(file_path):
    ### return 10-angle contrast of the image ###
    __DISTANCE = [1]
    __ANGLE = [0, numpy.pi/4, numpy.pi/2, numpy.pi*3/4, numpy.pi, numpy.pi*5/4, numpy.pi*3/2, numpy.pi*7/4]
    __LEVELS = 10

    img = cv2.imread(file_path, 0)
    gray_level_map = numpy.vectorize(get_gray_level)
    leveled = gray_level_map(img)
    glcm = greycomatrix(leveled, __DISTANCE, __ANGLE, levels=__LEVELS)
    contrast = greycoprops(glcm, 'contrast')
    return contrast


def get_glcm_dissimilarity(file_path):
    ### return 10-angle dissimilarity of the image ###
    __DISTANCE = [1]
    __ANGLE = [0, numpy.pi/4, numpy.pi/2, numpy.pi*3/4, numpy.pi, numpy.pi*5/4, numpy.pi*3/2, numpy.pi*7/4]
    __LEVELS = 10

    img = cv2.imread(file_path, 0)
    gray_level_map = numpy.vectorize(get_gray_level)
    leveled = gray_level_map(img)
    glcm = greycomatrix(leveled, __DISTANCE, __ANGLE, levels=__LEVELS)
    dissimilarity = greycoprops(glcm, 'dissimilarity')
    return dissimilarity


def get_glcm_homogeneity(file_path):
    ### return 10-angle homogeneity of the image ###
    __DISTANCE = [1]
    __ANGLE = [0, numpy.pi/4, numpy.pi/2, numpy.pi*3/4, numpy.pi, numpy.pi*5/4, numpy.pi*3/2, numpy.pi*7/4]
    __LEVELS = 10

    img = cv2.imread(file_path, 0)
    gray_level_map = numpy.vectorize(get_gray_level)
    leveled = gray_level_map(img)
    glcm = greycomatrix(leveled, __DISTANCE, __ANGLE, levels=__LEVELS)
    homogeneity = greycoprops(glcm, 'homogeneity')
    return homogeneity


def get_glcm_asm(file_path):
    ### return 10-angle asm of the image ###
    __DISTANCE = [1]
    __ANGLE = [0, numpy.pi/4, numpy.pi/2, numpy.pi*3/4, numpy.pi, numpy.pi*5/4, numpy.pi*3/2, numpy.pi*7/4]
    __LEVELS = 10

    img = cv2.imread(file_path, 0)
    gray_level_map = numpy.vectorize(get_gray_level)
    leveled = gray_level_map(img)
    glcm = greycomatrix(leveled, __DISTANCE, __ANGLE, levels=__LEVELS)
    asm = greycoprops(glcm, 'ASM')
    return asm


def get_glcm_energy(file_path):
    ### return 10-angle energy of the image ###
    __DISTANCE = [1]
    __ANGLE = [0, numpy.pi/4, numpy.pi/2, numpy.pi*3/4, numpy.pi, numpy.pi*5/4, numpy.pi*3/2, numpy.pi*7/4]
    __LEVELS = 10

    img = cv2.imread(file_path, 0)
    gray_level_map = numpy.vectorize(get_gray_level)
    leveled = gray_level_map(img)
    glcm = greycomatrix(leveled, __DISTANCE, __ANGLE, levels=__LEVELS)
    energy = greycoprops(glcm, 'energy')
    return energy


def get_glcm_correlation(file_path):
    ### return 10-angle correlation of the image ###
    __DISTANCE = [1]
    __ANGLE = [0, numpy.pi/4, numpy.pi/2, numpy.pi*3/4, numpy.pi, numpy.pi*5/4, numpy.pi*3/2, numpy.pi*7/4]
    __LEVELS = 10

    img = cv2.imread(file_path, 0)
    gray_level_map = numpy.vectorize(get_gray_level)
    leveled = gray_level_map(img)
    glcm = greycomatrix(leveled, __DISTANCE, __ANGLE, levels=__LEVELS)
    correlation = greycoprops(glcm, 'correlation')
    return correlation


def get_glcm_prop(file_path, prop):
    ### return 10-angle specified property of the image ###
    __DISTANCE = [1]
    __ANGLE = [0, numpy.pi/4, numpy.pi/2, numpy.pi*3/4, numpy.pi, numpy.pi*5/4, numpy.pi*3/2, numpy.pi*7/4]
    __LEVELS = 10

    img = cv2.imread(file_path, 0)
    gray_level_map = numpy.vectorize(get_gray_level)
    leveled = gray_level_map(img)
    glcm = greycomatrix(leveled, __DISTANCE, __ANGLE, levels=__LEVELS)
    glcm_prop = greycoprops(glcm, prop)
    return glcm_prop


def get_glcm_all_props(file_path):
    ### return 10-angle all properties of the image ###
    __DISTANCE = [1]
    __ANGLE = [0, numpy.pi/4, numpy.pi/2, numpy.pi*3/4, numpy.pi, numpy.pi*5/4, numpy.pi*3/2, numpy.pi*7/4]
    __LEVELS = 10

    img = cv2.imread(file_path, 0)
    gray_level_map = numpy.vectorize(get_gray_level)
    leveled = gray_level_map(img)
    glcm = greycomatrix(leveled, __DISTANCE, __ANGLE, levels=__LEVELS)
    all_props = {
        "contrast": greycoprops(glcm, 'contrast').tolist(),
        "dissimilarity": greycoprops(glcm, 'dissimilarity').tolist(),
        "homogeneity": greycoprops(glcm, 'homogeneity').tolist(),
        "asm": greycoprops(glcm, 'ASM').tolist(),
        "energy": greycoprops(glcm, 'energy').tolist(),
        "correlation": greycoprops(glcm, 'correlation').tolist()
    }
    # Note:
    # serializing numpy array
    # https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
    return all_props
