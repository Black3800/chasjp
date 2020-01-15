import cv2, math


class Piece:

    def __init__(self, img, n):
        self.img_path = "cropped/" + img + "/" + img + "_crop" + str(n) + ".png"
        img_m = cv2.imread(self.img_path)
        self.top = img_m[0, :]
        self.bottom = img_m[-1, :]
        self.left = img_m[:, 0]
        self.right = img_m[:, -1]


rank = []
puzzle = []
for i in range(0, 5):
    puzzle.append(Piece("autumn", i))
size = len(puzzle[0].right)

for i in range(0, 5):
    # right
    for j in range(i+1, 5):
        diff = 0
        for x in range(0, size-1):
            diff += math.sqrt((puzzle[i].right[x][0] - puzzle[j].left[x][0])**2 + (puzzle[i].right[x][1] - puzzle[j].left[x][1])**2 + (puzzle[i].right[x][2] - puzzle[j].left[x][2])**2)
        print(i, "<->", j, diff)
