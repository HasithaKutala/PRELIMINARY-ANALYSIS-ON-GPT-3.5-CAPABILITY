
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np
import re
class train_test_split():
        
    def func_split_train_test(cl,input_data):
       
        label_encoder = LabelEncoder()
        new_text = []
        for i in input_data['comment']:
            new_text.append(re.sub("\W"," ",str(i)))
        y = list(label_encoder.fit_transform(input_data['politeness']))
        X = new_text
       
        print(y)
        print(X)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test
    


