import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.dropna(subset = ['RUE_ACCDN'], inplace = True) # drop rows with missing street names

print(df[df['NB_MORTS'] > 0]['RUE_ACCDN'].value_counts().head(10)) # print the top 10 streets with the most deadly collisions

# plot with matplotlib (20 deadliest streets)
df[df['NB_MORTS'] > 0]['RUE_ACCDN'].value_counts().head(20).plot(kind='bar', title='Deadly road collisions by street name- Montreal', xlabel='Street name', ylabel='Total deadly collisions (2012-2022)' ,figsize=(10, 5)) 
plt.show()