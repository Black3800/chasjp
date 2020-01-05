import cv2
import math

# def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
#     dim = None
#     (h, w) = image.shape[:2]
#
#     if width is None and height is None:
#         return image
#     if width is None:
#         r = height / float(h)
#         dim = (int(w * r), height)
#     else:
#         r = width / float(w)
#         dim = (width, int(h * r))
#
#     return {
#         "image": cv2.resize(image, dim, interpolation=inter),
#         "width": dim[0],
#         "height": dim[1]
#     }


# imgname = input()
imgname = 'lighthouse'
# w, h = 780, 780
img = cv2.imread(imgname + '.jpg', 1)
src_height, src_width, src_channel = img.shape
w = src_width if (src_width < src_height) else src_height
h = src_height if (src_height < src_width) else src_width
# resize = ResizeWithAspectRatio(img, width=w)
# resize['image'] = resize['image'][0:w, 0:h]
img = img[0:w, 0:h]
# print(w, h)

c = 3
width_increment = int(w/c)
height_increment = int(h/c)
pieces = []

# for i in range(int(c*c)-1, -1, -1):
for i in range(int(c*c)):
    windowname = 'CV2 Image show ' + str(i)
    height_start = int(height_increment*math.floor(i/c))
    height_end = int(height_start + height_increment)
    width_start = int(width_increment*(i % c))
    width_end = int(width_start + width_increment)
    # print(windowname)
    pieces.append(img[height_start:height_end, width_start:width_end])
    # print(resize['image'][height_start:height_end, width_start:width_end][0][0])  # matrix
    # print("width: " + str(width_start) + " to " + str(width_end))
    # print("height: " + str(height_start) + " to " + str(height_end))
    # print("\n")
    cv2.namedWindow(windowname)
    cv2.imshow(windowname, img[height_start:height_end, width_start:width_end])
    cv2.moveWindow(windowname, width_start, height_start)

k = cv2.waitKey()

if k == ord('s'):
    cv2.imwrite(imgname+'_copy.png', pieces[4])

cv2.destroyAllWindows()
