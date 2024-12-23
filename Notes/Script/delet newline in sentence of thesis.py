import pyperclip

# conda install conda-forge::pyperclip

# 这个脚本是用来把pdf中论文复制下来的句子中的换行符去掉，然后复制到剪贴板中。

lines = []
print("请输入文本，输入两次回车键结束：")
while True:
    line = input()
    if not line:
        break
    lines.append(line)
    
text = ' '.join(lines)
print(text)

pyperclip.copy(text)
print("已复制到剪贴板")

