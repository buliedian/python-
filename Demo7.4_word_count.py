def count_words(filename):
    """计算文件有多少个单词"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
##        print(f'The file "{filename}" does not exist')
    else:
        # 计算文件有多少个单词
        words = contents.split()
        num_words = len(words)
        print(f'The file "{filename}" contains {num_words} words.')

filename1= r"E:\Desktop\源代码文件\源代码文件\chapter_10\alice.txt"
filename2= r"E:\Desktop\源代码文件\源代码文件\chapter_10\sidhartha.txt"
filename3= r"E:\Desktop\源代码文件\源代码文件\chapter_10\moby_dick.txt"
filename4= r"E:\Desktop\源代码文件\源代码文件\chapter_10\little_women.txt"
filenames=[filename1,filename2,filename3,filename4]
for filename in filenames:
    count_words(filename)

