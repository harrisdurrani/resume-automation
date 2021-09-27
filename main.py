import os
from dataclasses import dataclass

@dataclass
class Automate:

    path: str =  r'D:\PY Files\My Projects\resume-automation\Target'


    def read_files(self):
        files = os.listdir(self.path)

        for file in files:
            temp = file.split("_")
            print(temp)

if __name__ == "__main__":
    a = Automate()

    a.read_files()
