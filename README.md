# [Image Palette Detector](https://github.com/Gourieff/img-palette-detector)

This is a simple python application that detects dominant color of your source image and create an output palette combined with the source image.

## Installation

__Just download or clone the repo and install requirements:__
```
$ pip install -r requirements.txt
```
or
```
$ pip install opencv-python; colorthief
```

__If you want as a package for some reasons:__
```
$ pip install git+https://github.com/Gourieff/img-palette-detector
```

## Usage:

```
$ python ipd.py
```
Then you see the dialog:
```
> How to build Palette? (Choose 1, 2 or 3)
> 1 - OpenCV based method
> 2 - ColorThief based method
> 3 - Both
```
Type 1, 2 or 3 and proceed to the next step:
```
Type the filename or path (ex.: image.png):
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
How much colors on the Palette must be? (2 - is minimum, don't type too much, 3-7 is optimal)
```
And type how much color must be in the Palette, for example:
```
5
```
Then wait a little for the result.

## Example:

```
$ python ipd.py
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

![0](https://github.com/Gourieff/img-palette-detector/raw/main/sample/image.png)

__Output Result:__

Method 1:

![1](https://github.com/Gourieff/img-palette-detector/raw/main/sample/image_5-colors-palette_method-1.png)

Method 2:

![2](https://github.com/Gourieff/img-palette-detector/raw/main/sample/image_5-colors-palette_method-2.png)

For most images Method 1 is more accurate, but for some images (as shown above) Method 2 will give you a better result
