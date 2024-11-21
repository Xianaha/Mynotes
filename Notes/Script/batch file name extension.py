import os

# 假设有如下目录结构：
# Cats, Dogs, and Foxes
# ├── batch file name extension.py
# ├── cat/
# │   ├── cat001.jpg
# │   ├── cat002.jpg
# │   ├── cat003.jpg
# │   ├── cat004.jpg
# │   ├── cat005.jpg
# │   ├── ...
# ├── dog/
# │   ├── dog001.jpg
# │   ├── dog002.jpg
# │   ├── dog003.jpg
# │   ├── dog004.jpeg
# │   ├── dog005.jpeg
# │   ├── ...
# └── fox/
#     ├── fox001.jpg
#     ├── fox002.jpg
#     ├── fox003.jpg
#     ├── fox004.jpg
#     ├── fox005.jpg
#     ├── ...

def batch_file_name_extension(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for dir in dirs:
            class_dir = os.path.join(root, dir)
            for file in os.listdir(class_dir):
                file_path = os.path.join(class_dir, file)
                if os.path.splitext(file_path)[1] != ".jpg":
                    print(file_path + " is renamed to ", end="")
                    new_file_name = os.path.splitext(file_path)[0] + ".jpg"
                    os.rename(file_path, new_file_name)
                    print(new_file_name)
                    
if __name__ == "__main__":
    root_dir = "D:\Cats, Dogs, and Foxes"
    batch_file_name_extension(root_dir)