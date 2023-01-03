from rembg import remove
from PIL import Image
#import easygui as eg
input_path = 'krish.jpeg'
output_path = 'krish2.jpeg'
input = Image.open(input_path)
output = remove(input)

#im = Image.open("krish2.jpeg")
#rgb_im = im.convert('RGB')
#rgb_im.save('audacious.jpg')
output2 = output.convert('RGB')


output2.save(output_path)