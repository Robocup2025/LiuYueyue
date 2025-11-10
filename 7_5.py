import random
import pathlib
import string
import os

def create_file(folder_name):
    current_dir = pathlib.Path(__file__).parent.absolute()
    img_dir = current_dir / folder_name
    img_dir.mkdir(parents=True, exist_ok=True)
    for i in range(x):
        file_path=img_dir / f"test{i}.txt"
        with open(file_path,'w',encoding='utf-8') as f:
            for j in range(y):
                line=''.join(random.choices(string.ascii_letters+string.digits,k=6))
                f.write(line+'\n')

def change_file(folder_name):
    current_dir=pathlib.Path(__file__).parent.absolute()
    img_dir=current_dir / folder_name
    for i in range(x):
        old_file_path=img_dir / f"test{i}.txt"
        with open(old_file_path,'r') as f:
            lines=f.readlines()
            new_lines=[line.strip()+'-python\n' for line in lines]
        with open(old_file_path,'w') as f:
            f.writelines(new_lines)
        base, ext = os.path.splitext(old_file_path)
        new_file_name=base+"-python"+ext
        new_file_path=img_dir / new_file_name
        os.rename(old_file_path,new_file_path)

if __name__ == '__main__':
    x = int(input("请输入创建文件的个数："))
    y = int(input("请输入文件中字符的行数："))
    create_file("test")
    change_file("test")