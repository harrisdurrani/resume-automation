import os
from dataclasses import dataclass
from pathlib import Path
import shutil

def read_files():
    path = r""
    target = r""
    dir_list = os.listdir(path)
    for file in dir_list:
        temp = file.split("_")
        company_name = temp[1].strip(".txt")

        new_directory = os.path.join(target, company_name)
        print(new_directory)
        print(os.path.join(path, file))
        print(file)
        try:
            os.mkdir(new_directory)

        except FileExistsError:
            print("folder already exists")
        if file.endswith(".txt"):
            shutil.copy2(os.path.join(path, file), new_directory)

      

if __name__ == "__main__":
    read_files()
    # a = Automate()

    # a.read_files()
