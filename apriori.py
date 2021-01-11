import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Market_Basket_Optimisation.csv',header=None)

data=[]

for i in range(len(dataset)):
    data.append(list(dataset.iloc[i,:].dropna()))
    

from apyori import apriori


rules=apriori(data,min_support=0.003,min_confidence=0.2,min_lift=3,min_length=2)


for item in rules:  
    pair = item[0]   
    items = [x for x in pair]  
    print("Rule: " + items[0] + " -> " + items[1])  
  
    print("Support: " + str(item[1]))  
    print("Confidence: " + str(item[2][0][2]))  
    print("Lift: " + str(item[2][0][3]))  
    print("=====================================")  


















