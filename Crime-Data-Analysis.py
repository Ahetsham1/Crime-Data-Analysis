import seaborn as sns
import matplotlib.pyplot as plt
import pymysql
import pandas as pd
import warnings

warnings.filterwarnings("ignore")
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='Tajheer@12',
                       port=3307,
                       database='crime_data')
print(conn)

str1 = 'select * from crime_data'
df = pd.read_sql(str1, conn)
print(df)

# To find the Where are the geographical hotspots for reported crimes?
f = 'select LAT,LON from crime_data;'
g = pd.read_sql(f, conn)
plt.figure(figsize=(10, 5))
sns.scatterplot(x=g['LAT'], y=g['LON'], s=20, alpha=0.5)
plt.title('Geographical Hotspots For Reported Crimes', color='red')
plt.grid()
plt.show()

# What is the distribution of victim ages in reported crimes?
d = 'select Vict_Age from crime_data'
df = pd.read_sql(d, conn)
print(df)
plt.figure(figsize=(5, 5))
sns.histplot(x=df['Vict_Age'], bins=25, color='blue', edgecolor='black')
plt.title('Distribution of Victim Ages in Reported Crimes')
plt.xlabel('Vict_age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Is there a significant difference in crime rates between male and female victims?
p = "SELECT Vict_Sex, COUNT(*) as count FROM crime_data WHERE Vict_Sex IN ('M', 'F') GROUP BY Vict_Sex;"
df = pd.read_sql(p, conn)
print(df)
sns.countplot(data=df, x='Vict_Sex', palette='Set2', width=0.2)
plt.xlabel('Victim gendar')
plt.ylabel('Number of crimes')
plt.title('significant difference in crime rates between male and female victim')
plt.show()

# Where do most crimes occur based on the "Location" column?
h = 'SELECT Location, COUNT(*) AS crime_count FROM crime_data GROUP BY Location ORDER BY crime_count DESC LIMIT 5;'
df = pd.read_sql(h, conn)
print(df)
plt.figure(figsize=(10, 5))
plt.bar(df['Location'], df['crime_count'], width=0.3)
plt.xlabel('Location ')
plt.ylabel('crime count')
plt.title('Most Crimes Occur Based On The "Location" Column')
plt.show()

# What is the distribution of reported crimes based on Crime Code?
f = 'select Crm_Cd from crime_data;'
df = pd.read_sql(f, conn)
plt.figure(figsize=(10, 6))
plt.hist(df['Crm_Cd'], bins=50, color='cyan', edgecolor='black', width=10)
plt.xlabel('Crime Code')
plt.ylabel('Frequency')
plt.title('Distribution Of Reported Crimes Based On Crime Code')
plt.grid(True)
plt.show()

conn.close()
