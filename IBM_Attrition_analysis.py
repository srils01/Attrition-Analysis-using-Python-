
# Importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%


# Reading the csv file
df=pd.read_csv("/Users/harishsarvepalli/Github_projects/WA_Fn-UseC_-HR-Employee-Attrition 2.csv")

#Data Wrangling
def data_wrangling():

    # Displaying the number of rows and columns
    print(df.shape)
    #Displaying the column names
    print(df.columns)
    #Checking the data type
    print(df.dtypes)
    # Checking for any missing values
    print(df.isna().sum())
    #Displaying the first 5 rows
    print(df.head(5))
    #Checking for duplicate values
    print(df.duplicated().sum())
    #Dropping the columns that are not required
    df.drop('DailyRate','Education','RelationshipSatisfaction','EmployeeNumber','MaritalStatus',axis=1,inplace=True)


# Data Analysis
def data_analysis1():

    #Exploratory data analysis
    print(df.describe())


    # Count the number of exits (Filtering the Attrition column)
    print(df.Attrition.value_counts())
    filtered_df = df[df['Attrition'] == 'Yes']
    attrition_count_df = filtered_df.groupby('Department')[['Attrition']].agg('count')
    print(attrition_count_df)
    percentage_of_total=attrition_count_df.Attrition/attrition_count_df.Attrition.sum()*100
    print(percentage_of_total)
    sizes=percentage_of_total
    labels=['Human Resources','R&D','Sales']
    plt.pie(sizes,labels=labels,autopct='%1.1f%%')
    plt.title('Attrition by department')
    plt.show()



def data_analysis2():
    filtered_df_Gender = df[df['Attrition'] == 'Yes']
    gender_pivot_table=pd.pivot_table(data=filtered_df_Gender,index='Department',columns='Gender',values='Attrition',aggfunc='count')
    print(gender_pivot_table)
    gender_pivot_table.plot(kind='bar')
    plt.xlabel('Department')
    plt.ylabel('Gender')
    plt.title('Gender wise Attrition')
    plt.show()


def data_analysis3(): 
    # Relation between job satisfaction and Attrition
    filtered_df=df[df['Attrition']=='Yes']
    job_satisfaction_pivot_table=pd.pivot_table(data=filtered_df,index='JobSatisfaction',columns='Department',values='Attrition',aggfunc='count')
    print(job_satisfaction_pivot_table)
    job_satisfaction_pivot_table.plot(kind='bar')
    plt.xlabel('JobSatisfaction')
    plt.ylabel('Number of exits')
    plt.show()
     
def data_analysis4():
# # # Bucketing the Tenure into years category

    tenure=[]


    for value in df.YearsAtCompany:
        if value>=0 and value<1:
            tenure.append('0-1 years')
        elif value>=1 and value<3:
            tenure.append('1-3 years')
        elif value>=3 and value<5:
            tenure.append('3-5 years')
        elif value>=5 and value<10:
            tenure.append('5-10 years')
        else:
            tenure.append('>10 years')       
    
    df['Tenure with the company']=tenure
    # print(df.Tenure with the company.head(5))
    # print(df.columns)

# # New joinee attrition-Department wise
    filtered_df_newjoinee=df[df['Attrition']=='Yes']
    # filtered_df_Tenure=df[df['Tenure with the company']=='0-1 years']
    newjoine_table=pd.pivot_table(data=filtered_df_newjoinee,index='Tenure with the company',columns='Department',values='Attrition',aggfunc='count')
    print(newjoine_table)
    newjoine_table.plot(kind='bar')
    plt.xlabel('Tenure with the company')
    plt.ylabel('Department')
    plt.title('Attrition-Tenure wise')
    plt.show()

def data_analysis5():

# # # Career growth Vs attrition


    tenure_promotion=[]


    for value in df.YearsSinceLastPromotion:
        if value>=0 and value<1:
            tenure_promotion.append('0-1 years')
        elif value>=1 and value<3:
            tenure_promotion.append('1-3 years')
        elif value>=3 and value<5:
            tenure_promotion.append('3-5 years')
        elif value>=5 and value<10:
            tenure_promotion.append('5-10 years')
        else:
            tenure_promotion.append('>10 years')       

    df['Time since last promotion']=tenure_promotion
    print(df['Time since last promotion'].head(5))

    filtered_df=df[df['Attrition']=='Yes']
    # filtered_df_Tenure_in_current_level=df[df['Tenure_in_current_level']=='3-5 years']
    promotion_table=pd.pivot_table(data=filtered_df,index='Time since last promotion',columns='Department',values='Attrition',aggfunc='count')
    print(promotion_table)

    promotion_table.plot(kind='bar')
    plt.xlabel('Time since last promotion')
    plt.ylabel('Department')
    plt.title('Career growth Vs Attrition')
    plt.show()

# # Performance rating vs Number of exits

    filtered_df_pr = df[df['Attrition'] == 'Yes']
    performance_table=pd.pivot_table(data=filtered_df_pr,index='PerformanceRating',values='Attrition',aggfunc='count')
#     # attrition_count_pr_df = filtered_df.groupby('PerformanceRating')[['Attrition']].agg('count')
    print(performance_table)

def data_analysis6():

# # Salary hikes Vs Attrition

    attrition=df[df['Attrition'] == 'Yes']
    salary_hike__table=pd.pivot_table(data=attrition,index='PercentSalaryHike',values='Attrition',aggfunc='count')
    print(salary_hike__table)

    plt.scatter(salary_hike__table.index, salary_hike__table['Attrition'])
    plt.xlabel('Percentage of Salary Hiked')
    plt.ylabel('Attrition')
    plt.title('Percentage of Salary Hiked vs. Attrition') 
    plt.show() 

def data_analysis7():

# # Salary hikes Vs tenure in the company
    hike_table_df=pd.pivot_table(data=df,index='YearsAtCompany',values='PercentSalaryHike',aggfunc='mean')
    # filter_df=df.groupby('PercentSalaryHike')[['YearsAtCompany']].agg('count')
    # print(filter_df)
    print(hike_table_df)
    hike_table_df.plot(kind='line')
    plt.xlabel("years at company")
    plt.ylabel('percentage of salary hike')
    plt.show()
 



def data_analysis():
    
    user_input=input("What do you want to analyze?"
    "Enter 1 for attrition- department wise"
    "Enter 2 for gender wise Attrition"
    "Enter 3 for Job satisfaction vs number of exits"
    "Enter 4 for Tenure wise attrition"
    "Enter 5 for career growth vs number of exits"
    "Enter 6 for Salary hikes vs number of exits"
    "Enter 7 for Salary hikes vs ")
    if user_input=='1':
        data_analysis1()
    elif user_input=='2':
        data_analysis2()
    elif user_input=='3':
        data_analysis3()
    elif user_input=='4':
        data_analysis4()
    elif user_input=='5':
        data_analysis5()
    elif user_input=='6':
        data_analysis6()
    elif user_input=='7':
        data_analysis7()
    else:
        print("enter the correct input")
    




data_wrangling()
data_analysis()
















# %%
