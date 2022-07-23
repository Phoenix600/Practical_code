# import modules here 
import pandas as pd
import numpy as np
exam_data = {
        'name' : ['Ajay','Vijay','Vivek','Atharv','Apurva','Rupal','Priyal','Srushti','Pranay','Vishal'],
        'score'     :   [12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts'  :   [1,3,2,3,2,3,1,1,2,1],
        'qualify'   :   ['yes','no','yes','no','no','yes','yes','no','no','yes'],
        
        }
labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(exam_data,index=labels)
print(df)
# check point-01 :
#print(df[['name','score']].describe())
print(df[['name','score']])
# check-point-02 : 
print(df[df['score'].between(15,20)])
# check point-03 :
print(df[df['score'].isnull()])
# check point-04 :
df.loc['d','score'] = 11.5
print(df)
# check point-05 :
print(df['attempts'].sum())
