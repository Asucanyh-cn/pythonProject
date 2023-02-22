'''
encoding:utf-8
author:yh
date:2022/5/9 19:02
'''
# pip install textblob --no-deps
from textblob import TextBlob
tb = TextBlob("TextBlob aims to provide access to common "
              "text-processing operations through afamiliar interface.")
print(tb.tags)
print(tb.noun_phrases)
print(tb.words)
testimonial = TextBlob("Python is an amazing programming language.")
print(testimonial.sentiment)
print(testimonial.sentiment.polarity)
print(testimonial.sentiment.subjectivitys)
