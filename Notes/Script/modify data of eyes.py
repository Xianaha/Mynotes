import os

def modify_labels(directory):
    # 遍历指定目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):  # 假设标签文件以.txt结尾
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()  # 读取文件内容

                # 对每一行进行修改
                modified_lines = []
                for line in lines:
                    # 这里可以根据需要进行相应的修改
                    modified_line = line.strip()
                    modified_line = modified_line.replace("0.0", "0.5")
                    modified_lines.append(modified_line)

                # 将修改后的内容写回文件
                with open(file_path, 'w') as f:
                    f.write('\n'.join(modified_lines))

                print(f"{file} 已修改.")

if __name__ == "__main__":
    labels_directory = 'D:\Code\VScode_Python\dataset\labels\\test'  # 修改为你的train文件夹路径
    modify_labels(labels_directory)
    labels_directory = 'D:\Code\VScode_Python\dataset\labels\\val'  # 修改为你的train文件夹路径
    modify_labels(labels_directory)
    
