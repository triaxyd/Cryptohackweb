from PIL import Image, ImageChops

image_path1 = "GENERAL/XOR/lemurxor/flag_7ae18c704272532658c10b5faad06d74.png"
image_path2 = "GENERAL/XOR/lemurxor/lemur_ed66878c338e662d3473f0d98eedbd0d.png"

image1 = Image.open(image_path1)
image2 = Image.open(image_path2)

image3 = ImageChops.add(ImageChops.subtract(image2, image1), ImageChops.subtract(image1, image2))
image3.show()






