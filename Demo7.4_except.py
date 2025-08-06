filename='data/alice.txt'
try:
    with open(filename,encoding='utf-8') as f:
          contents=f.read()
except FileNotFoundError:
    print(f'The {filename} file does not exist')
else:
    #计算文件有多少个单词
    words=contents.split()
    num_words=len(words)
    print(f'The file {filename} has {num_words} words')
          
