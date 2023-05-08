import os
import shutil

path = "../img"

for filename in os.listdir(path):
    file_str = str(filename)[4:6]
    file_id = int(file_str)
    if (file_id > 10 and file_id < 37):
        file_name_alphabet = chr(file_id - 11 + 65)
        dir_name = file_name_alphabet + " UPPER"
        if (os.path.isdir(f"../{dir_name}")):
            shutil.move(f"{path}/{filename}", f"../{dir_name}")
        else:
            os.mkdir(f"../{dir_name}")
            shutil.move(f"{path}/{filename}", f"../{dir_name}")

    elif (file_id > 36):
        file_name_alphabet = chr(file_id - 37 + 97)
        dir_name = file_name_alphabet + " LOWER"
        if (os.path.isdir(f"../{dir_name}")):
            shutil.move(f"{path}/{filename}", f"../{dir_name}")
        else:
            os.mkdir(f"../{dir_name}")
            shutil.move(f"{path}/{filename}", f"../{dir_name}")

    else:
        if (os.path.isdir(f"../{file_str}")):
            shutil.move(f"{path}/{filename}", f"../{file_str}")
        else:
            os.mkdir(f"../{file_str}")
            shutil.move(f"{path}/{filename}", f"../{file_str}")
