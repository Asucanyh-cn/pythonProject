'''
encoding:utf-8
author:yh
date:2022/4/4 20:17
'''
import pandas as pd
from sklearn.datasets import load_iris
iris_dataset=load_iris()
iris=pd.DataFrame(iris_dataset.data,columns=['SpealLength','Spealwidth'])