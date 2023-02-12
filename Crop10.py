import math
from PIL import Image
import os
working_dir = r'C:/Users/Ros/Магистратура/NIR/dataset/NIR/Test/'
out_dir = r'C:/Users/Ros/Магистратура/NIR/'
for filename in os.listdir(working_dir):
   with Image.open(os.path.join(working_dir, filename)) as image:   
        x, y=image.size
        width=x*9//10
        height=y*4//5
        x=x//5
        y=y//10
        image.crop((x, y, width, height)).save(os.path.join(out_dir, filename))