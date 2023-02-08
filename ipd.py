# -*- coding: utf-8 -*-
"""
    Image Palette Detector
    ~~~~~~~~~~
    Fast and accurate image RGB palette detector by Eugene Gourieff.
    :copyright: (c) 2023 by Eugene Gourieff.
    :license: GPL-3.0, see LICENSE for more details.
"""

__version__ = '0.3.0'

import modules.fileTasks as fT
import modules.inputDialogs as iD
import modules.main as ipd
import modules.gui as UI
import argparse
import PySimpleGUI as sg

is_arg = [0,0,0,0]

parser = argparse.ArgumentParser(description='Fast and accurate image RGB palette detector by Eugene Gourieff.')
# parser.add_argument('filename', metavar='I', help='Path to the image file')
parser.add_argument('-i', dest='path_to_image', action='store', required=False, help='Path to the image file')
parser.add_argument('-m', dest='method', action='store', required=False, help='Method to build Palette: 1 - OpenCV based method, 2 - ColorThief based method, 3 - Both')
parser.add_argument('-c', dest='colors_count', action='store', required=False, help="How much colors on the Palette must be: 2 - is minimum, don't type too much, 3-7 is optimal")
parser.add_argument('-d', dest='dialog_mode', action='store_true', required=False, help="To run Application in the dialog mode w/o GUI")
args = parser.parse_args()
img_file = args.path_to_image
p_method = args.method
color_c = args.colors_count
dialog_mode = args.dialog_mode
if img_file:
    print(img_file)
    is_arg[0] = 1
if p_method == '1' or p_method == '2' or p_method == '3':
    print(p_method)
    is_arg[1] = 1
if color_c:
    color_c = int(color_c)
    print(color_c)
    is_arg[2] = 1
    if color_c < 2: color_c = 2
    elif color_c > 24: color_c = 24
if dialog_mode:
    print('Running in no-gui dialog mode...')
    is_arg[3] = 1

# input dialog: ask method and filename
if is_arg[1] == 0 and is_arg[3] == 1: p_method = iD.set_method()
if is_arg[1] == 0 and is_arg[3] == 0: p_method = UI.set_method()
if is_arg[0] == 0 and is_arg[3] == 1: img_file = iD.f_name()
if is_arg[0] == 0 and is_arg[3] == 0: img_file = UI.get_file()

# check file exists or not
fT.is_f_exist(img_file)

# getting extension and striped filename, extract the file name (with path) and extension and check whether it is an image or not
img_n, img_e = fT.f_split(img_file)

# input dialog: ask for number of colors in Palette
if is_arg[2] == 0 and is_arg[3] == 1: color_c = iD.colors_num()
if is_arg[2] == 0 and is_arg[3] == 0: color_c = UI.colors_num()

print('Detecting... Please wait...')

# sending params:
if p_method == '1': ipd.cv2_method(img_file, img_n, img_e, color_c)
elif p_method == '2': ipd.ct_method(img_file, img_n, img_e, color_c)
elif p_method == '3':
    ipd.cv2_method(img_file, img_n, img_e, color_c)
    print('Detecting... Please wait...')
    ipd.ct_method(img_file, img_n, img_e, color_c)