# Image Palette Detector

This is a simple python application that detects dominant color of your source image and create an output palette combined with the source image.

**Guide:**  
[**Interface**](#interface)  
[**Installation**](#installation)  
[**Usage**](#usage)  
[**Example**](#example)

## Interface

Application has 3 types of the user-interface:
* the comand-line with arguments:

<img src="https://github.com/Gourieff/img-palette-detector/raw/main/docs/img/cl-mode.jpg" alt="cl-mode" width="50%"/>

* the dialog with no-GUI:

<img src="https://github.com/Gourieff/img-palette-detector/raw/main/docs/img/no-gui-dialog-mode.jpg" alt="no-gui-dialog-mode" width="50%"/>

* the dialog with GUI:

<img src="https://github.com/Gourieff/img-palette-detector/raw/main/docs/img/gui-dialog-mode.jpg" alt="gui-dialog-mode" width="50%"/>

## Installation

__Just [download](https://github.com/Gourieff/img-palette-detector/archive/refs/heads/main.zip) or clone the repo__
```
git clone https://github.com/Gourieff/img-palette-detector
```
__and install requirements:__
```
pip install -r requirements.txt
```
or
```
pip install opencv-python; colorthief; argparse; pysimplegui
```
__You can also install it as a package:__
```
pip install imgpd
```

<!---
__If you want to use as a package for some reasons:__
```
pip install git+https://github.com/Gourieff/img-palette-detector
```
--->

## Usage:

```
python ipd.py -i "C:\my super images\image_file_name.png" -m "3" -c "5"
```
**If you installed as a package:**

> for Windows users

```
py -m imgpd -i "C:\my super images\image_file_name.png" -m "3" -c "5"
```
> for Linux/MacOS users:

```
imgpd -i /home/user/images/image_file_name.png -m 3 -c 5
```

> Where optional arguments are:
```
  -i PATH_TO_IMAGE  Path to the image file
  -m METHOD         Method to build the Palette: 1 - OpenCV based method, 2 - ColorThief based method, 3 - Both
  -c COLORS_COUNT   How much colors on the Palette must be: 2 - is minimum, don't type too much, 3-7 is optimal
  -d                To run Application in the dialog mode w/o GUI
```
or just type for help: `python ipd.py -h` or `imgpd -h`

**You can also run the App in the dialog mode**

> with GUI:

`python ipd.py` or `imgpd`

> without GUI:

`python ipd.py -d` or `imgpd -d`

Then you see the dialog:
```
> How to build Palette? (Choose 1, 2 or 3)
> 1 - OpenCV based method
> 2 - ColorThief based method
> 3 - Both
```
Type 1, 2 or 3 and proceed to the next step:
```
> Type the filename or path (ex.: image.png):
```
Type a full or a relative path to your image or just an image name if your image is at the same folder:
```
C:\my super images\image_file_name.png
```
or
```
/home/user/images/image_file_name.png
```
or
```
image_file_name.png
```
Proceed to the next step:
```
> How much colors on the Palette must be? (2 - is minimum, don't type too much, 3-7 is optimal)
```
And type how much color must be in the Palette, for example:
```
5
```
Then wait a little for the result.

## Example:

```
$ imgpd -d
> How to build Palette? (Choose 1, 2 or 3)
> 1 - OpenCV based method
> 2 - ColorThief based method
> 3 - Both
>> 3
> Type the filename or path (ex.: image.png):
>> sample/image.png
> How much colors on the Palette must be? (2 - is minimum, don't type too much, 3-7 is optimal)
>> 5
```

__Source Image:__

<img src="https://github.com/Gourieff/img-palette-detector/raw/main/sample/image.png" alt="image" width="50%"/>

__Output Result:__

Method 1:

<img src="https://github.com/Gourieff/img-palette-detector/raw/main/sample/image_5-colors-palette_method-1.png" alt="image_5-colors-palette_method-1" width="63%"/>

Method 2:

<img src="https://github.com/Gourieff/img-palette-detector/raw/main/sample/image_5-colors-palette_method-2.png" alt="image_5-colors-palette_method-2" width="63%"/>

For most images Method 1 is more accurate, but for some images (as shown above) Method 2 will give you a better result, so I recommend to use 'Both' and then choose which is better.
