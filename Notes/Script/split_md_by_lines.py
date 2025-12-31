#!/usr/bin/env python3
"""
将markdown文件按行分割成多个子文件

用法：
    python split_md_by_lines.py input.md [--lines N] [--output-dir DIR]

示例：
    python split_md_by_lines.py document.md --lines 250
"""

import os
import sys
import argparse
from pathlib import Path

def split_md_file(input_file, lines_per_file=250, output_dir=None):
    """
    将markdown文件按行分割成多个子文件
    
    参数：
        input_file (str): 输入markdown文件的路径
        lines_per_file (int): 每个输出文件的行数
        output_dir (str, optional): 输出目录。如果为None，则在输入文件所在目录下
                                   创建名为"{输入文件名}_split"的目录
    """
    input_path = Path(input_file)
    
    # 检查输入文件是否存在
    if not input_path.exists():
        print(f"错误：输入文件 '{input_file}' 不存在。")
        sys.exit(1)
    
    # 确定输出目录
    if output_dir is None:
        output_dir = input_path.parent / f"{input_path.stem}_split"
    else:
        output_dir = Path(output_dir)
    
    # 如果输出目录不存在则创建
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 读取输入文件
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"读取文件 '{input_file}' 时出错：{e}")
        sys.exit(1)
    
    total_lines = len(lines)
    if total_lines == 0:
        print(f"警告：输入文件 '{input_file}' 为空。")
        return
    
    # 计算输出文件数量
    num_files = (total_lines + lines_per_file - 1) // lines_per_file
    
    print(f"正在分割 '{input_file}' ({total_lines} 行) 成 {num_files} 个文件")
    print(f"  - 每文件行数：{lines_per_file}")
    print(f"  - 输出目录：{output_dir}")
    
    # 分割并写入文件
    file_count = 0
    for i in range(0, total_lines, lines_per_file):
        file_count += 1
        chunk = lines[i:i + lines_per_file]
        
        # 生成输出文件名
        output_file = output_dir / f"{input_path.stem}_{file_count:03d}{input_path.suffix}"
        
        # 写入块到文件
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.writelines(chunk)
            print(f"  已创建：{output_file.name} ({len(chunk)} 行)")
        except Exception as e:
            print(f"写入文件 '{output_file}' 时出错：{e}")
    
    print(f"\n完成！在 '{output_dir}' 中创建了 {file_count} 个文件")

def main():
    parser = argparse.ArgumentParser(
        description="将markdown文件按行分割成多个子文件",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "input_file",
        help="输入markdown文件的路径"
    )
    
    parser.add_argument(
        "-l", "--lines",
        type=int,
        default=250,
        help="每个输出文件的行数（默认：250）"
    )
    
    parser.add_argument(
        "-o", "--output-dir",
        help="输出目录。如果未指定，则在输入文件所在目录下创建名为"
             "'{输入文件名}_split'的目录"
    )
    
    args = parser.parse_args()
    
    split_md_file(
        input_file=args.input_file,
        lines_per_file=args.lines,
        output_dir=args.output_dir
    )

if __name__ == "__main__":
    main()
