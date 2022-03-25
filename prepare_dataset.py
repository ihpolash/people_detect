import re
import requests
import os, sys
from os import listdir
from PIL import Image

def prepare_dataset(file, save_dir):

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    with open(file) as f:
        urls = f.read()
        links = re.findall('"((http)s?://.*?)"', urls)

    for url in links:
        img_data = requests.get(url[0]).content
        file_name = save_dir + str(url[0].split("?")[0].split("/")[-1])
        with open(file_name, 'wb') as handler:
            handler.write(img_data)

    for filename in listdir(save_dir):
        if filename.endswith('.jpg'):
            try:
                img = Image.open(save_dir+filename)  # open the image file
                img.verify()  # verify that it is, in fact an image
            except (IOError, SyntaxError) as e:
                print(filename)
                os.remove(save_dir+filename)
    return "Successful!"

file = sys.argv[1]
save_dir = sys.argv[2]

prepare_dataset(file, save_dir)

