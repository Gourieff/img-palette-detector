import os,sys
from PIL import Image, ImageDraw

def is_f_exist(fname):
    # check file exists or not
    if os.path.exists(fname): print('File exists -- ok')
    elif fname == '': sys.exit('Canceled')
    else: sys.exit(fname + ' does not exist')

def f_remove(fname):
    if os.path.exists(fname): os.remove(fname)

def f_split(fname):
    split_f = os.path.splitext(fname)
    img_n = split_f[0]
    img_e = split_f[1].lower()
    e_supported = ['.png','.jpg','.jpeg','.bmp']
    if img_e in e_supported: 
        print(f'File extension: {img_e}')
        return img_n, img_e
    else: sys.exit(img_e + ' is the wrong extension of an image file')

def img_resolution(fname):
    # load the image through PIL
    image = Image.open(fname)
    # get img resolution
    width, height = image.size
    return image, width, height