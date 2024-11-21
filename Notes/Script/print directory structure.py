import os

def print_directory_structure(directory, prefix='', max_items=5):
    items = os.listdir(directory)  # 列出目录下的所有文件和文件夹
    count = len(items)              # 获取项目总数

    for index, item in enumerate(items):
        item_path = os.path.join(directory, item)  # 获取项目的完整路径
        is_last = index == count - 1                # 判断当前项目是否为最后一个项

        if index < max_items:  # 只显示最多 max_items 个项目
            # 添加树状结构的符号并打印项目
            if is_last:
                print(f"{prefix}└── {item}/" if os.path.isdir(item_path) else f"{prefix}└── {item}")
                new_prefix = prefix + '    '  # 更新前缀
            else:
                print(f"{prefix}├── {item}/" if os.path.isdir(item_path) else f"{prefix}├── {item}")
                new_prefix = prefix + '│   '  # 更新前缀

            # 如果是目录，则递归调用
            if os.path.isdir(item_path):
                print_directory_structure(item_path, new_prefix)
        elif index == max_items:  # 显示省略号
            print(f"{prefix}├── ...")  # 省略号表示还有其他项目
        # 超过 max_items 的项目将被忽略，不打印其内容

if __name__ == "__main__":
    root_directory = 'D:\\Code\\VScode_Python\\datasets\\Cats, Dogs, and Foxes'  # 替换为你要遍历的目录路径
    print_directory_structure(root_directory)
