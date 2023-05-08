from PIL import Image
import numpy as np
import os

path = "./dataset"
i = 0
j = 0

DATASET = []
LABELS = np.array(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

for dir_name in os.listdir(path):
    if i > 0:
        break
    i += 1
    arr = []
    for filename in os.listdir(f"{path}/{dir_name}"):
        if j > 0:
            break
        img_path = f"{path}/{dir_name}/{filename}"
        image = Image.open(img_path)
        img_array = np.array(image)
        arr.append(img_array)
        j += 1
    DATASET.append(arr)

DATASET = np.array(DATASET)
print(len(DATASET))
