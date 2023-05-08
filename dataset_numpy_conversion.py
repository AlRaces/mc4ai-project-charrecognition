from PIL import Image, ImageOps
import numpy as np
import os

path = "./dataset"
DATASET = []
LABELS = []

for dir_name in os.listdir(path):
    LABELS.append(dir_name.split()[0])
    arr = []
    for filename in os.listdir(f"{path}/{dir_name}"):
        img_path = f"{path}/{dir_name}/{filename}"
        image = Image.open(img_path)
        image = image.resize((28, 28))
        image = ImageOps.grayscale(image)
        img_array = np.array(image)
        arr.append(img_array)
    DATASET.append(arr)

DATASET = np.array(DATASET)
np.save("./np_dataset.npy", DATASET)
LABELS = np.array(LABELS)
np.save("./labels.npy", LABELS)
