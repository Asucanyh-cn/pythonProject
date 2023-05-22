'''
encoding:utf-8
author:yh
date:2023/4/10 10:32
'''
from textblob import TextBlob
#1）分词
# tb = TextBlob("TextBlob aims to provide access to common text-processing operations through a familiar interface.")
# print(tb.tags)
# print(tb.noun_phrases)
# print(tb.words)
# #textblob不仅可以根据空格分词，还可以根据逗号！
# animals = TextBlob("apple,elephant,octopus,peach!")
# print(animals.words)
# print(animals.words.pluralize()) #复数形式
#2）情感分析
# testimonial = TextBlob("Python is an amazing programming language. It's very good!")
# print(testimonial.sentiment) #polarity取值[-1,1]，表示正面或负面；subjectivity取值[0,1]，表示客观程度，越小越客观。

# zen = TextBlob("Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.")
# print(zen.words)
# print(zen.sentences)
# #对每个句子再做情感分析
# for sentence in zen.sentences:
#     print(sentence.sentiment)

# x=TextBlob("I am a good student. I try to study python!")
# print(x.words)
# print(x.sentences)
# print(x.sentiment)
# #对每个句子再做情感分析
# for i in x.sentences:
#     print(i.sentiment)
#
# hello = TextBlob("We are saying hello to you.We are now saying hello, hello, HELLO to you.")
# print(hello.word_counts['hello'])
# print(hello.words.count('hello', case_sensitive=True))
# #n-grams 是指给定的一段文本或语音中 N 个项目（item）的序列
# blob = TextBlob("What you say is very funny.")
# print(blob.ngrams(n=3))
# #贝叶斯模型文本分类
# from textblob.classifiers import NaiveBayesClassifier
# train = [
#     ('I love this sandwich.', 'pos'),
#     ('this is an amazing place!', 'pos'),
#     ('I feel very good about these beers.', 'pos'),
#     ('this is my best work.', 'pos'),
#     ("what an awesome view", 'pos'),
#     ('I do not like this restaurant', 'neg'),
#     ('I am tired of this stuff.', 'neg'),
#     ("I can't deal with this", 'neg'),
#     ('he is my sworn enemy!', 'neg'),
#     ('my boss is horrible.', 'neg')
# ]
# cl = NaiveBayesClassifier(train)
# # print(cl)
# # result=cl.classify("This is an amazing library!")
# # print(result)
#
# prob_dist = cl.prob_classify("you do not like me.") #预测概率分布
# print(prob_dist.max()) #最终结果 neg
# print(round(prob_dist.prob("pos"), 2)) #预测是 pos 的概率
# print(round(prob_dist.prob("neg"), 2)) #预测是 neg 的概率
#
# blob = TextBlob("The beer is good. But the hangover is horrible.",classifier=cl)
# print(blob.classify())
# for s in blob.sentences:
#     print(s+' 分类结果：'+s.classify())