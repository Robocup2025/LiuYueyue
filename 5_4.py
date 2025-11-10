import pathlib
import os
import random
import string

def f(folder_name,num,extension):
    current_dir=pathlib.Path(__file__).parent.absolute()
    img_dir=current_dir / folder_name
    img_dir.mkdir(parents=True,exist_ok=True)
    for i in range(num):
        file_name=''.join(random.choices(string.ascii_letters+string.digits,k=4))+extension
        file_path=img_dir / file_name
        file_path.touch()

if __name__ == '__main__':
    f('img',100,'.png')