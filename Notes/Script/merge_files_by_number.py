#!/usr/bin/env python3
"""
按照文件名中的数字顺序合并指定目录下的文件

用法：
    python merge_files_by_number.py input_dir [--output OUTPUT] [--pattern PATTERN]

示例：
    python merge_files_by_number.py ./split_files --output merged.md --pattern "*.md"
    将./split_files目录下所有.md文件按照文件名中的数字顺序合并到merged.md
注意：
    1. 合并时不会插入任何分隔符或额外内容
    2. 输出文件的扩展名会与输入文件保持一致（如果未指定输出文件）
"""

import os
import sys
import argparse
import re
from pathlib import Path
import glob

def extract_number(filename):
    """
    从文件名中提取数字
    
    参数：
        filename (str): 文件名
        
    返回：
        int: 提取到的数字，如果没有数字则返回0
    """
    # 使用正则表达式查找文件名中的第一个连续数字串
    match = re.search(r'(\d+)', filename)
    if match:
        return int(match.group(1))
    return 0

def get_common_extension(sorted_files):
    """
    获取文件列表中第一个文件的扩展名，假设所有文件扩展名相同
    
    参数：
        sorted_files: 排序后的文件信息列表
        
    返回：
        str: 文件扩展名（包含点），如".md"
    """
    if not sorted_files:
        return ".txt"
    
    first_file = sorted_files[0]['path']
    return Path(first_file).suffix

def merge_files_by_number(input_dir, output_file=None, pattern="*"):
    """
    按照文件名中的数字顺序合并文件
    
    参数：
        input_dir (str): 输入目录路径
        output_file (str, optional): 输出文件路径。如果为None，则自动生成merged.{ext}，其中ext为输入文件的扩展名
        pattern (str): 文件匹配模式，如"*.md"、"*.txt"等
    """
    input_path = Path(input_dir)
    
    # 检查输入目录是否存在
    if not input_path.exists() or not input_path.is_dir():
        print(f"错误：输入目录 '{input_dir}' 不存在或不是目录。")
        sys.exit(1)
    
    # 获取匹配的文件列表
    search_pattern = str(input_path / pattern)
    files = glob.glob(search_pattern)
    
    if not files:
        print(f"警告：在目录 '{input_dir}' 中没有找到匹配模式 '{pattern}' 的文件。")
        return
    
    print(f"在目录 '{input_dir}' 中找到 {len(files)} 个匹配文件")
    
    # 提取文件名和数字，用于排序
    file_info = []
    for file_path in files:
        file_name = os.path.basename(file_path)
        number = extract_number(file_name)
        file_info.append({
            'path': file_path,
            'name': file_name,
            'number': number
        })
    
    # 按照数字从小到大排序
    sorted_files = sorted(file_info, key=lambda x: x['number'])
    
    # 输出排序结果供用户检查
    print("按数字排序的文件列表：")
    for i, file_info in enumerate(sorted_files, 1):
        print(f"  {i:3d}. {file_info['name']} (数字: {file_info['number']})")
    
    # 确定输出文件路径
    if output_file is None:
        # 获取通用扩展名
        ext = get_common_extension(sorted_files)
        output_file = input_path / f"merged{ext}"
    else:
        output_file = Path(output_file)
    
    # 确保输出文件的目录存在
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # 合并文件
    total_lines = 0
    total_bytes = 0
    try:
        with open(output_file, 'w', encoding='utf-8') as out_f:
            for file_info in sorted_files:
                file_path = file_info['path']
                file_name = file_info['name']
                
                # 读取并写入文件内容，不添加任何分隔符
                try:
                    with open(file_path, 'r', encoding='utf-8') as in_f:
                        content = in_f.read()
                        out_f.write(content)
                        lines = content.count('\n') + 1
                        total_lines += lines
                        total_bytes += len(content)
                        
                        print(f"  已合并: {file_name} ({lines} 行)")
                except UnicodeDecodeError:
                    # 如果utf-8解码失败，尝试用二进制模式读取
                    try:
                        with open(file_path, 'rb') as in_f:
                            content = in_f.read()
                            # 尝试用其他常见编码解码
                            for encoding in ['gbk', 'latin-1', 'cp1252']:
                                try:
                                    text = content.decode(encoding)
                                    out_f.write(text)
                                    lines = text.count('\n') + 1
                                    total_lines += lines
                                    total_bytes += len(text)
                                    print(f"  已合并: {file_name} ({lines} 行, 编码: {encoding})")
                                    break
                                except UnicodeDecodeError:
                                    continue
                            else:
                                # 所有编码都失败，用二进制写入（对于二进制文件，我们无法合并到文本文件中）
                                # 这里选择跳过，只记录警告
                                print(f"  警告: {file_name} 是二进制文件，跳过内容")
                    except Exception as e:
                        print(f"  错误: 读取文件 {file_name} 时出错: {e}")
                except Exception as e:
                    print(f"  错误: 读取文件 {file_name} 时出错: {e}")
        
        print(f"\n完成！已合并 {len(sorted_files)} 个文件到 '{output_file}'")
        print(f"总行数: {total_lines}")
        print(f"总字节数: {total_bytes}")
        
    except Exception as e:
        print(f"写入输出文件时出错: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="按照文件名中的数字顺序合并指定目录下的文件",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "input_dir",
        help="包含要合并的文件的目录路径"
    )
    
    parser.add_argument(
        "-o", "--output",
        help="输出文件路径。如果未指定，则自动生成merged.{ext}，其中ext为输入文件的扩展名"
    )
    
    parser.add_argument(
        "-p", "--pattern",
        default="*",
        help="文件匹配模式（例如：'*.md', '*.txt', 'full_*.md'）。默认：'*'（所有文件）"
    )
    
    args = parser.parse_args()
    
    merge_files_by_number(
        input_dir=args.input_dir,
        output_file=args.output,
        pattern=args.pattern
    )

if __name__ == "__main__":
    main()
