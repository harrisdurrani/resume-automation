import os
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Automate:

    file_path: str = Path.cwd() / "Target"

    def read_files(self,target=r"C:\Users\harri\Documents\Resume"):
        files = os.listdir(self.file_path)

        for file in files:
            temp = file.split("_")
            company_name = temp[1].strip(".txt")
            try:
                new_path = os.path.join(target, company_name)
                os.mkdir(new_path)
            except FileExistsError:
                print("folder already exists")

        print(target)

                
if __name__ == "__main__":
    a = Automate()

    a.read_files()
