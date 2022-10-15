import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.dropna(subset = ['RUE_ACCDN'], inplace = True) # drop rows with missing street names

print(df['RUE_ACCDN'].value_counts().head(10)) # print the top 10 streets with the most collisions

# plot with matplotlib (20 most dangerous streets)
df['RUE_ACCDN'].value_counts().head(20).plot(kind='bar', title='Road collisions by street name- Montreal', xlabel='Street name', ylabel='Total accidents (2012-2022)' ,figsize=(10, 5))
plt.show()