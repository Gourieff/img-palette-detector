def set_method():
    method = '0'
    while int(method) != 1 and int(method) != 2 and int(method) != 3:
        method = input('How to build Palette? (Choose 1, 2 or 3)\n1 - OpenCV based method\n2 - ColorThief based method\n3 - Both\n')
    else:
        return method

def f_name():
    file = input('Type the filename or path (ex.: image.png): ')
    if file == '': file = 'image.png' # by default
    return file

def colors_num():
    num = int(input("How much colors on the Palette must be? (2 - is minimum, don't type too much, 3-7 is optimal) "))
    if num < 2: num = 2
    if num > 24:
        print("Don't be crazy! This's too much! Lowering to 24")
        num = 24
    return num