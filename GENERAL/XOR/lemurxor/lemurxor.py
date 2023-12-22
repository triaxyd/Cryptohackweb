from pwn import xor
from PIL import Image,ImageChops
import numpy as np


image1 = Image.open("lemurxor/flag_7ae18c704272532658c10b5faad06d74.png")
image2 = Image.open("lemurxor/lemur_ed66878c338e662d3473f0d98eedbd0d.png")

image3 = ImageChops.add(ImageChops.subtract(image2, image1), ImageChops.subtract(image1, image2))
image3.show()







