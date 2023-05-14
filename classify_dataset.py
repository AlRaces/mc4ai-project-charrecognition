import os
import shutil


def main():
    path = "../img"
    for filename in os.listdir(path):
        file_str = str(filename)[4:6]
        file_id = int(file_str)

        file_id -= 1
        if (os.path.isdir(f"../{str(file_id)}")):
            shutil.move(f"{path}/{filename}", f"../{str(file_id)}")
        else:
            os.mkdir(f"../{str(file_id)}")
            shutil.move(f"{path}/{filename}", f"../{str(file_id)}")


if __name__ == "main":
    main()
