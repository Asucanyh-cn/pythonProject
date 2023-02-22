'''
encoding:utf-8
author:yh
date:2022/5/16 10:17
'''
def load_dict(filename):
    word_dict = set()
    max_len = 1
    f = open(filename,'r', encoding='UTF-8')
    for line in f:
        word = str(line.strip())
        word_dict.add(word)
        if len(word)> max_len:
            max_len = len(word)
    return  max_len, word_dict

def fmm_word_seg(sent,max_len,word_dict):
    end= len(sent)
    words = []
    sent = str(sent)
    while end > 0:
        for begin in range(end - max_len,end):
            if sent[begin:end] in word_dict:
                words.append(sent[begin:end])
                break
        end = begin
    return words


#max_len,word_dict=load_dict('d:/dict1.txt')
max_len,word_dict=load_dict('d:/dict2.txt')
print(word_dict)
#sent = input('Input a sentence:')
#sent = '我在北京天安门学习历史知识。'
sent = '有意见分歧'
words = fmm_word_seg(sent,max_len,word_dict)
for word in words:
    print(word)
