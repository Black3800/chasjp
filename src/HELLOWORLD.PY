import cv2

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return {
        "image": cv2.resize(image, dim, interpolation=inter),
        "width": dim[0],
        "height": dim[1]
    }


imgname = input()
# imgname = 'student'
img = cv2.imread(imgname + '.jpg', 1)
resize = ResizeWithAspectRatio(img, None, height=600)['image']
# resize = cv2.arrowedLine(resize['image'], (0,0), (int(resize['width']/2), int(resize['height']/2)), (255,0,5), 5)

img1 = resize[0:200, 0:200]
img2 = resize[0:200, 200:400]

cv2.imshow('CV2 Image Show', img1)
cv2.imshow('CV2 Image Show2', img2)
k = cv2.waitKey(10000)

if k == ord('s'):
    cv2.imwrite(imgname+'_copy.png', resize)

cv2.destroyAllWindows()
