
# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading csv files 
df=pd.read_csv("/Users/harishsarvepalli/Github_projects/ReactionTypes (1).csv")
df2=pd.read_csv("/Users/harishsarvepalli/Github_projects/Reactions (1).csv")
df3=pd.read_csv("/Users/harishsarvepalli/Github_projects/Content (1).csv")

# Data wrangling

# Checking for missing/null values
print(df.isna().sum())
print(df2.isna().sum())
print(df3.isna().sum())

# Dropping the columns that are not needed for the analysis and that have missing values
drop_url=df3.dropna(axis=1,inplace=True)
print(df3.isna().sum())

drop_userid=df2.drop(['User ID'],axis=1,inplace=True)
print(df2.isna().sum())
drop_type_null=df2.dropna(axis=0,subset=["Type"],inplace=True)
print(df2)

# Checking the datatype of columns

print(df.dtypes)
print(df2.dtypes)
print(df3.dtypes)

# Cleaning the string values to a unique format

df3.Category=df3.Category.str.replace('"', ' ')
print(df3.Category)


# Merging the csv files and creating a combined dataframe
merged_df = pd.merge(df2, df3, on='Content ID', how='left')
print(merged_df)
merged_df=merged_df.rename(columns={'Type_x':'Type'})
merged_df=pd.merge(merged_df,df,on='Type',how='left')
print(merged_df)

# Adding up the total score for each category
merged_df.Category=merged_df.Category.str.strip()
merged_df.Category=merged_df.Category.str.title()
print(merged_df.Category.value_counts())

# getting the top 5 popular content categories
table=pd.pivot_table(data=merged_df,index=['Category'],values=['Score'],aggfunc='sum')
print(table)
print(table.sort_values(['Score'],ascending=False).head(5))

# Plotting graphs

# Top 5 popular content categories

table.plot(kind='bar')
plt.xlabel('Content categories')
plt.ylabel('Sum of scores')
plt.title('Content Categories by popularity')
plt.show()

# Reactions on Content by users
table2=pd.pivot_table(data=merged_df, index='Type',values='Score', aggfunc='count')
print(table2)
table2.plot(kind='bar')
plt.xlabel('Reaction Type')
plt.ylabel('Number of reactions')
plt.title('Reactions on Content by users')
plt.show()



# merged_df.sentiment=pd.merge(merged_df,df,on='')
table3=pd.pivot_table(data=merged_df,index='Sentiment',values='Score',aggfunc='count')
print(table3)


sizes=[56.19,12.5,31.3]
labels=['Positive','Neutral','Negative']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Sentiment Analysis')
plt.show()
















