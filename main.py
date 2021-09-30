import os
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Automate:

    path: str = Path.cwd() / "Target"

    def read_files(self):
        files = os.listdir(self.path)

        for file in files:
            temp = file.split("_")
            print(temp)

if __name__ == "__main__":
    a = Automate()

    a.read_files()
