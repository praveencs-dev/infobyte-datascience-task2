import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("D:\\datascience\\task2\\csvfile1.csv")
df.columns=[col.strip().replace('\ufeff','') for col in df.columns]
df['Date']=pd.to_datetime(df['Date'],dayfirst=True)
df['year']=df['Date'].dt.year
average=df.groupby('year')['Estimated Unemployment Rate (%)'].mean().reset_index()
plt.figure(figsize=(14,6))
sns.barplot(data=average,x='year',y='Estimated Unemployment Rate (%)',color='salmon')
plt.tight_layout()
plt.show()
