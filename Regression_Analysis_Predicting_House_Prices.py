#!/usr/bin/env python
# coding: utf-8

# # Regression Analysis: Predicting House Prices
# 
# 

# In[ ]:





# In[ ]:





# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

np.random.seed(42)
data = {'SquareFootage': np.random.randint(800, 3000, 100),
        'NumBedrooms': np.random.randint(1, 5, 100),
        'HousePrice': 50000 + 300 * np.random.randn(100)}
df = pd.DataFrame(data)

X = df[['SquareFootage', 'NumBedrooms']]
y = df['HousePrice']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

plt.scatter(y_test, predictions)
plt.xlabel('Actual House Prices')
plt.ylabel('Predicted House Prices')
plt.title('Regression Analysis: Predicted vs. Actual House Prices')
plt.show()


# In[ ]:





# In[ ]:




