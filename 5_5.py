import random
import pathlib

def f(num,extension):
    current_dir=pathlib.Path(__file__).parent
    img_dir=current_dir / 'img'
    all_files=list(img_dir.glob('*'))
    choose_files=random.sample(all_files,num)
    for file in choose_files:
        base=file.stem
        new_name=base+extension
        file_path=img_dir / new_name
        file.rename(file_path)

if __name__=='__main__':
    f(50,'.jpg')