import os


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