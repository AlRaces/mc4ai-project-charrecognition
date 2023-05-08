from PIL import Image
import numpy as np
import os

path = "./dataset"
for dir_name in os.listdir(path):
    for filename in os.listdir(f"{path}/{dir_name}"):
        pass
