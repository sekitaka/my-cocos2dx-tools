# 一番左上のピクセルと同じピクセルは全て透過させる

__author__ = 'takashi'
from PIL import Image
IN_FILE = 'image.png'       # 入力ファイル
OUT_FILE = 'out_image.png'  # 結果出力ファイル

# debug
# 参考
# http://effbot.org/imagingbook/introduction.htm
image = Image.open(IN_FILE)
# print(image.size)
# print(image.mode)
# print(image.info)
# print(image.text)

# 元の画像のサイズ
width = image.size[0]
height = image.size[1]

# 結果出力用画像オブジェクト
outImage = Image.new(image.mode, image.size, "black") # create a new black image
outPixels = outImage.load() # create the pixel map

basePixels = image.load()
defaultPixel = image.getpixel((0,0)) # 左上のピクセルの値のタプル
clearPixel = (0,0,0,0) # 透過ピクセルのタプル

for i in range(width):
    for j in range(height):
        pixel = basePixels[i,j]
        if(pixel == defaultPixel):
            outPixels[i,j] = clearPixel
        else:
            outPixels[i,j] = pixel

# 変換した画像を出力
outImage.save(OUT_FILE,'PNG')
