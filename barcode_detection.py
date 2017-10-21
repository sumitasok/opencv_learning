import numpy as np
import argparse
import cv2

# sublime snippet from https://github.com/Stibbons/sublime-user-config
parser = ArgumentParser(description="barcode scanner")
parser.add_argument("-i", "--image", dest="destination member name",
                        help="path to the image file", required=True)
# Process arguments
args = parser.parse_args(argv)