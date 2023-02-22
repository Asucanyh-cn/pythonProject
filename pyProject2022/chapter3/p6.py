'''
encoding:utf-8
author:yh
date:2022/4/4 20:06
'''
import matplotlib.pyplot as plt


ax2 = fig.add_subplot(2,2,2)
plt.bar(range(4),[3,4,2,3],width=0.3)
plt.xticks(x,s,rotation=90)