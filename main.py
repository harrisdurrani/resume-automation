import os
from dataclasses import dataclass

@dataclass
class Automate:

    path: str =  r'D:\PY Files\My Projects\resume-automation\Target'


    def get_path(self):
        files = os.listdir(self.path)

        for file in files:
            print(file)

if __name__ == "__main__":
    a = Automate()

    a.get_path()