import cv2
import modules.getPalette as gP
import modules.fileTasks as fT
from PIL import Image, ImageDraw
from colorthief import ColorThief

def cv2_method(img_file, img_n, img_e, color_c):
    # load the image through cv2
    img = cv2.imread(img_file)

    # get the dominant color palette
    palette = gP.dominant_color(img, color_c)

    # print the dominant colors
    print("Dominant Colors:")
    for color in palette:
        print(color)

    palette_num = len(palette)
    print(f'The Number of dominant colors detected: {palette_num}')

    # get img resolution
    image, width, height = fT.img_resolution(img_file)

    width_c = round(width*0.35)

    height_block = round(height/color_c)-2

    # create blank image through PIL
    button_img = Image.new('RGB', (width+width_c+10,height), "white")

    # create a new image to draw the rectangles on
    draw = ImageDraw.Draw(button_img)
    button_img.save(img_n+'_blank'+img_e)

    # load blank image through cv2
    img_palette = cv2.imread(img_n+'_blank'+img_e)

    # create rectngles through cv2
    for i, color in enumerate(palette):
        x,y = 10, 10 + (i * height_block)
        color = (int(color[0]),int(color[1]),int(color[2]))
        cv2.rectangle(img_palette, (x,y), (x+width_c-10, y+height_block-10), tuple(color), -1)

    # save pallete to blank image through cv2
    cv2.imwrite(img_n+'_blank'+img_e, img_palette)

    # load, combine and save the result through PIL
    img_palette = Image.open(img_n+'_blank'+img_e)
    img_palette.paste(image, (width_c+10, 0))
    img_palette.save(img_n+'_'+str(color_c)+'-colors-palette'+'_method-1'+img_e)

    # remove blank palette file
    fT.f_remove(img_n+'_blank'+img_e)

    print('Done!')

def ct_method(img_file, img_n, img_e, color_c):
    # getting img through colorthief
    color_thief = ColorThief(img_file)
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)
    # build a color palette
    palette = color_thief.get_palette(color_count=color_c,quality=1)

    print('The most Dominant Color:')
    print(dominant_color)

    #replacing first one to dominant (just in case):
    palette[0] = dominant_color
    print("Dominant Colors:")

    for color in palette:
        print(color)

    palette_num = len(palette)
    print(f'The Number of dominant colors detected: {palette_num}')
    if palette_num < color_c:
        print(f'<Less than requested>\nThe Number of color on the Palette is set to: {palette_num}')
        color_c = int(palette_num)

    # load the image
    image = Image.open(img_file)

    # get img resolution
    width, height = image.size

    height_c = height
    width_c = round(width*0.35)

    height_block = round(height_c/color_c)-2

    # create blank image
    button_img = Image.new('RGB', (width+width_c+10,height), "white")

    # create a new image to draw the rectangles on
    draw = ImageDraw.Draw(button_img)

    # loop through the dominant colors and draw rectangles
    for i, color in enumerate(palette):
        xy = (10, 10 + (i * height_block), width_c, height_block + (i * height_block))
        draw.rectangle(xy, fill=color)

    # paste source image to pallete
    button_img.paste(image, (width_c+10, 0))

    # save the image with the rectangles
    button_img.save(img_n+'_'+str(color_c)+'-colors-palette'+'_method-2'+img_e)

    print('Done!')