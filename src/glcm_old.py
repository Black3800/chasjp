import cv2, numpy

GRAY_THRESHOLD = [0, 25, 50, 75, 100, 125, 151, 177, 203, 229, 256]


def get_gray_level(gray_val):
    arr = GRAY_THRESHOLD
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


def horizontal_glcm(file_path):
    ### read file ###
    img = cv2.imread(file_path, 0)
    size = img.shape[0]

    ### compute ###
    sum = 0
    glcm = [[0]*10 for i in range(10)]
    for i in range(size):
        for j in range(size-1):
            from_level = get_gray_level(img[i][j])
            to_level = get_gray_level(img[i][j+1])
            glcm[from_level][to_level] += 1
            sum += 1

    glcm_transpose = numpy.transpose(glcm)
    glcm_sum = numpy.add(glcm, glcm_transpose)
    glcm_prob = numpy.multiply(glcm_sum, (1/sum))
    return glcm_prob


def vertical_glcm(file_path):
    ### read file ###
    img = cv2.imread(file_path, 0)
    size = img.shape[0]

    ### compute ###
    sum = 0
    glcm = [[0]*10 for i in range(10)]
    for i in range(size):
        for j in range(size-1):
            from_level = get_gray_level(img[j][i])
            to_level = get_gray_level(img[j+1][i])
            glcm[from_level][to_level] += 1
            sum += 1

    glcm_transpose = numpy.transpose(glcm)
    glcm_sum = numpy.add(glcm, glcm_transpose)
    glcm_prob = numpy.multiply(glcm_sum, (1/sum))
    return glcm_prob


def diagonal_glcm(file_path):
    ### read file ###
    img = cv2.imread(file_path, 0)
    size = img.shape[0]

    ### compute ###
    # sum = 0
    glcm = [[0]*10 for i in range(10)]
    for i in range(size-1):
        for j in range(size-1):
            from_level = get_gray_level(img[i][j])
            to_level = get_gray_level(img[i+1][j+1])
            glcm[from_level][to_level] += 1
            sum += 1

    glcm_transpose = numpy.transpose(glcm)
    glcm_sum = numpy.add(glcm, glcm_transpose)
    glcm_prob = numpy.multiply(glcm_sum, (1/sum))
    return glcm_prob


"""

00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33

03
02 13
01 12 23
00 11 22 33
10 21 32
20 31
30

03 02 13 01 12 23 00 11 22 33 10 21 32 20 31

0010120123123233

0
01
012
0123
123
23

full = n
cap = 1
start = 0
now = start
def abc:
    print now++
    if cap:
	if full:
            cap--
            start++
	else:
            cap++
	    now = start


function abc()
{
	k = now++
	if(now == cap)
	{
		if(cap == full)
		{
			inc = -1
			start++
		}
		cap += inc
		now = start
	}
	return k
}	


i=0
s=""
while(i<16)
{
	s += abc()
	i++
}
console.log(s)

"""