
# Importing Libraries
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import plotly as plty 
import plotly.express as px

# Reading the file
df=pd.read_csv("/Users/harishsarvepalli/Github_projects/Data Science Jobs Salaries.csv")
print(df)
print(df.columns.values)

#Data Cleaning
df.info(verbose=False)
print(df.isna().sum())
print(df.describe())
print(df.head())
print(df.job_title.value_counts())
df.job_title=df.job_title.replace("Finance Data Analyst", "Financial Data Analyst")
print(df.job_title.value_counts())

# Exploratory Data Analysis
 #  Which role has the highest salary?
print(df[df.salary_in_usd==df.salary_in_usd.max()])
print("The highest paid role is Principal Data Engineer")
#  Result by running the above code- Principal Data Engineer

 # Which employment types do employers prefer to hire?
employment_preference=df.employment_type.value_counts()
employment_preference.plot(kind='bar')
plt.xlabel('employment_type')
plt.ylabel('Number of employees hired')
plt.title('Types of employment')
plt.show()

print("The employer prefers to hire more for full time roles")
# Result by running the above code- FT

# Which role are entry leveled generally hired for?
print(df.experience_level.value_counts())
df_emp=df[df['experience_level']=='EN']
table=df_emp.pivot_table(index=["job_title"],columns=["experience_level"],values=["employment_type"],aggfunc='count')
print(table)
print(table.dropna(subset=[('employment_type', 'EN')]))
print("Data scientist role is the most hired one")
table.plot(kind='bar')
plt.xlabel('job_title')
plt.ylabel('experience_level')
plt.show()
# Result by running the above code- Data Scientist

# Which countries pay the highest for which roles?
table=pd.pivot_table(data=df,index=["job_title"],columns=["company_location"],values=["salary_in_usd"],aggfunc='max')
print(table)
print(df.salary_in_usd.max())
print(df.loc[193,'company_location'])
print("US pays the highest for Principal Data Engineer")

# Result by running the above code- US

# Which experience level has the highest hiring?

highest_hiring=df.experience_level.value_counts()
print(F"The experience level that has the highest hiring is :{highest_hiring}")
highest_hiring.plot(kind='bar')
plt.xlabel('Experience Level')
plt.ylabel('Count')
plt.title('Highest Hiring by Experience Level')
plt.show()


# Does company size affect the rate of hiring and pay scale?

count=df.company_size.value_counts()
print(count)
pivot=pd.pivot_table(data=df,index=["company_size"],values=["salary_in_usd"],columns=["employment_type"],aggfunc='sum')
print(pivot)
print("The level of hiring does not depend on the company size. Mid size companies seem to have highest hiring rates and highest salaries for full time and part time")

# What is the year over year (YoY) salary growth at different levels?
pivot_salary=pd.pivot_table(data=df,index=["work_year"],values=["salary_in_usd"],columns=["experience_level"],aggfunc='sum')
print(pivot_salary)
pivot_salary.plot(kind='line')
plt.xlabel('Year')
plt.ylabel('Salary')
plt.title('Year on Year Salary of company size')
plt.show()















