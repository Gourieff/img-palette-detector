import modules.fileTasks as fT
import modules.inputDialogs as iD
import modules.main as ipd

# input dialog: ask method and filename
p_method = iD.set_method()
img_file = iD.f_name()

# check file exists or not
fT.is_f_exist(img_file)

# getting extension and striped filename, extract the file name (with path) and extension and check whether it is an image or not
img_n, img_e = fT.f_split(img_file)

# input dialog: ask for number of colors in Palette
color_c = iD.colors_num()

print('Detecting... Please wait...')

# sending params:
if p_method == '1': ipd.cv2_method(img_file, img_n, img_e, color_c)
elif p_method == '2': ipd.ct_method(img_file, img_n, img_e, color_c)