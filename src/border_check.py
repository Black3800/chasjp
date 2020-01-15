import cv2
# from src.border import *


def f(x, y):
    return (x*y) % 2 == 0


result = []
size = 5
for i in range(0, 20):
    first = (i % size) + (int(i/size)*size*2)
    second = first + size
    print(first, second)
    result.append( f(first, second) )


print(result)
