# -*- coding: utf-8 -*-
import numpy as np
import argparse
import cv2

# sublime snippet from https://github.com/Stibbons/sublime-user-config
parser = argparse.ArgumentParser(description='barcode scanner')
parser.add_argument('-i', '--image', dest='image',
                    help='path to the image file', required=True)
# Process arguments
args = vars(parser.parse_args())

image = cv2.imread(args['image'])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

grayX = cv2.Sobel(gray, ddepth=cv2.CV_8UC1, dx=1, dy=0, ksize=-1)
grayY = cv2.Sobel(gray, ddepth=cv2.CV_8UC1, dx=0, dy=1, ksize=-1)

gradient = cv2.subtract(grayX, grayY)

kernel = (9, 9)
blurred = cv2.blur(gradient, kernel)

(_, thresh) = cv2.threshold(blurred, 47, 225, cv2.THRESH_BINARY)

kernelMorp = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernelMorp)

closedEr = cv2.erode(closed, None, iterations=15)
closedDil = cv2.dilate(closedEr, None, iterations=15)

(_, cnts, _) = cv2.findContours(closedDil.copy(),
                                cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))

cv2.drawContours(image, [box], -1, (0, 255, 0), 3)

cv2.imwrite(args['image'] + '.found.png', image)
