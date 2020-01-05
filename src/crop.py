import cv2, math, os
# import json

### read image ###
img_name = 'student'
img = cv2.imread("img/" + img_name + '.jpg', 1)
src_height, src_width, src_channel = img.shape

### prepare the process ###
size = 5
width = src_width if (src_width < src_height) else src_height
width = math.floor(width/size) * size
height = width
width_increment = int(width / size)
height_increment = int(height / size)
pieces = []
# img = img[0:width, 0:height]

### prepare the directory ###
dir_name = "cropped/" + img_name + "/"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

### crop and save ###
for i in range(int(size * size)):
    height_start = int(height_increment * math.floor(i / size))
    width_start = int(width_increment * (i % size))
    height_end = height_start + height_increment
    width_end = width_start + width_increment
    # file_name = dir_name + img_name + '_crop' + str(i) + '.png'
    cropped = img[height_start:height_end, width_start:width_end].copy()
    cv2.imwrite(dir_name + img_name + '_crop' + str(i) + '.png', cropped)
    pieces.append(cropped)

### report ###
print("cropped " + str(width) + "x" + str(width) + " into " + str(size * size) + " pieces")

# save as json
# file = open(dir_name + img_name + ".json", "w")
# file.write(json.dumps(pieces))
# file.close()
