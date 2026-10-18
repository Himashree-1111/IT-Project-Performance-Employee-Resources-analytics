import pandas as pd
import matplotlib.pyplot as plt

#==================================================================================================
#Employees analysis
#==================================================================================================
Employees=pd.read_csv("employee250.csv")
print(Employees.head())
print(Employees.shape)
print(Employees.isnull().sum())
print(Employees.columns)
print(Employees.isnull().sum())
print(Employees.duplicated().sum())
print(Employees.dtypes)
print(Employees.describe())
print(Employees["Salary_INR"].max())
print(Employees["Salary_INR"].min())
print(Employees["Department"].value_counts())
Employees["Salary_INR"]=pd.to_numeric(Employees["Salary_INR"],errors="coerce")
print(Employees["Salary_INR"].dtype)
print(Employees.groupby("Department")["Salary_INR"].mean().round(2).sort_values(ascending=False))
print(Employees["Salary_INR"].mean())
print(Employees["Experience_Years"].value_counts().sort_index())
print(Employees.groupby("Experience_Years")["Salary_INR"].mean().round(2))
print(Employees["Performance_Rating"].value_counts().sort_index())
print(Employees["Performance_Rating"].mean())
high_salary=Employees[Employees["Salary_INR"]>800000]
print(high_salary.shape[0])
print(high_salary[
    ["Employee_ID","Employee_Name","Department","Salary_INR"]])
highest_paid=Employees.loc[Employees["Salary_INR"].idxmax()]
print(highest_paid)
#===============================================================================================
#projects analysis
#==================================================================================================
projects=pd.read_csv("projects.csv")
print(projects.head())
#Check Rows and columns
print(projects.shape)
#Check column names
print(projects.columns)
#Check missing values
print(projects.isnull().sum())
#Check duplicate values
print(projects.duplicated().sum())
#Check data types
print(projects.dtypes)
#Statistical summary
print(projects.describe())
#Total projects
print(projects["Project_ID"].count())
#project by Status
print(projects["Status"].value_counts())
#Project by Technology
print(projects["Technology"].value_counts())
#total project budget
print(projects["Budget_INR"].sum())
#Total project revenue
print(projects["Revenue_INR"].sum())
#Average project Revenue
print(round(projects["Revenue_INR"].mean(),2))
#project with high revenue
print(projects["Revenue_INR"].max())
#highest project budget
print(projects.loc[
    projects["Revenue_INR"].idxmax(),
    ["Project_ID","Project_Name","Client","Revenue_INR"]])
#Project with highest revenue
print(projects.loc[
    projects["Revenue_INR"].idxmax(),["Project_ID","Project_Name","Client","Budget_INR"]])
#Highest project budget
print(projects["Budget_INR"].max())
#project with highest budget
print(projects["Budget_INR"].max())
#projects with revenue above $1crore
high_revenue=projects[projects["Revenue_INR"]>1000000]
print(high_revenue.shape[0])
#Average budget by technology
print(projects.groupby("Technology")["Budget_INR"].mean().round().sort_values(ascending=False))
#project count by client
print(projects["Client"].value_counts())
#Average revenue by client
print(projects.groupby("Client")["Revenue_INR"].mean().round(2).sort_values(ascending=False))
#Budget vs revenue
projects["Profit_INR"]=projects["Revenue_INR"]-projects["Budget_INR"]
print(projects[["Project_ID","Budget_INR","Revenue_INR","Profit_INR"]].head())
#Total profit
print(projects["Profit_INR"].sum())
print(round(projects["Profit_INR"].mean(),2))
#=================================================================================================
#PROJECT ALLOCATION analysis
#====================================================================================================
allocation=pd.read_csv("project allocation.csv")
#Load dataset
print(allocation.head())
#Check Row and Columns
print(allocation.shape)
#Check column names
print(allocation.columns)
#Check duplicates
print(allocation.duplicated().sum())
#Check Datatype
print(allocation.dtypes)
#statistical summary
print(allocation.describe())
#Total Allocation Records
print(allocation["Allocation_ID"].count())
#Employees Allocated to projects
print(allocation["Employee_ID"].nunique())
#Projects with Employee allocations
print(allocation["Project_ID"].nunique())
#Allocation by role
print(allocation["Role"].value_counts())
#Average allocation Percentage
print(round(allocation["Allocation_Percent"].mean(),2))
#Average Hours Worked
print(round(allocation["Hours_Worked"].mean(),2))
#Total hours worked
print(allocation["Hours_Worked"].max())
#Employees With Highest Hours
print(allocation.loc[allocation["Hours_Worked"].idxmax()])
#Average Hours By role
print(allocation.groupby("Role")
       ["Hours_Worked"].mean().round(2).sort_values(ascending=False))
#Total Hours by role
print(allocation.groupby("Role")
      ["Hours_Worked"].sum().sort_values(ascending=False))
#Average Allocation by role
print(allocation.groupby("Role")
      ["Allocation_Percent"].mean().round(2).sort_values(ascending=False))
#Total hours by project
print(allocation.groupby("Project_ID")["Hours_Worked"].sum().sort_values(ascending=False))
#=================================================================================================
#IT tickets analysis
#====================================================================================================
#Load the dataset
tickets=pd.read_csv("IT_tickets.csv")
print(tickets.head())
#Check size
print(tickets.shape)
#Check columns
print(tickets.columns)
#Missing values
print(tickets.isnull().sum())
#Duplicate Rows
print(tickets.duplicated().sum())
#Data types
print(tickets.dtypes)
#Tickets Count
print(tickets["Ticket_ID"].count())
#Tickets by priority
print(tickets["Priority"].value_counts())
#Tickets by issue type
print(tickets["Status"].value_counts())
#Number of projects with tickets
print(tickets["Project_ID"].nunique())
#Tickets Per project
print(tickets["Project_ID"].value_counts().sort_values(ascending=False))
#Critical Tickets
critical_tickets=tickets[tickets["Priority"]=="Critical"]
print(critical_tickets.shape[0])
#Critical tickets by issue type
print(critical_tickets["Issue_Type"].value_counts())
#Tickets by priority and status
print(pd.crosstab(tickets["Priority"],tickets["Status"]))
#Convert Dates
tickets["Created_Date"] = pd.to_datetime(
    tickets["Created_Date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

tickets["Resolved_Date"] = pd.to_datetime(
    tickets["Resolved_Date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)
#Average resolution time
tickets["Resolved_Date"] = pd.to_datetime(
    tickets["Resolved_Date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

# Calculate resolution days
tickets["Resolution_Days"] = (
    tickets["Resolved_Date"] - tickets["Created_Date"]
).dt.days

# Average resolution time
print(round(tickets["Resolution_Days"].mean(), 2))

# Longest resolution time
print(tickets["Resolution_Days"].max())
#=====================================================================================================
#monthly performance analysis
#=====================================================================================================
performance=pd.read_csv("monthly performance.csv")
print(performance.head())
#Check size
print(performance.shape)
#Check column names
print(performance.columns)
#check missing values
print(performance.isnull().sum())
#Check duplicates
print(performance.duplicated().sum())
#Check data types
print(performance.dtypes)
#Stastical summary
print(performance.describe())
#total records
print(performance.shape[0])
#number of projects
print(performance["Project_ID"].nunique())
#Total planned hours
print(performance["Planned_Hours"].sum())
#Total actual Hours
print(performance["Actual_Hours"].sum())
#Average Planned hours
print(round(performance["Planned_Hours"].mean(),2))
#Average Actual Hours
print(round(performance["Actual_Hours"].mean(),2))
#total tasks completed
print(performance["Tasks_Completed"].sum())
#Total bugs
print(performance["Bugs"].sum())
#Average Client Satisfaction
print(round(performance["Client_Satisfaction"].mean(),2))
#Highest client satisfaction
print(performance["Client_Satisfaction"].max())
#Lowest client satisfaction
print(performance["Client_Satisfaction"].min())
#Find Projects with the most bugs
print(performance.groupby("Project_ID")["Bugs"].sum().sort_values(ascending=False))
#Find projects with most completed tasks
print(performance.groupby("Project_ID")["Client_Satisfaction"].mean().round(2).sort_values(ascending=False))
#Calculate extra hours
performance["Extra_Hours"]=(performance["Actual_Hours"]-performance["Planned_Hours"])
print(performance[["Project_ID","Planned_Hours","Actual_Hours","Extra_Hours"]].head())
#Projects Exceeding planned hours
over_budget_hours=performance[performance["Actual_Hours"]>performance["Planned_Hours"]]
print(over_budget_hours.shape[0])
#Total extra hours
print(performance["Extra_Hours"].sum())
#Average extra hours
print(round(performance["Extra_Hours"].mean(),2))
#using matplotlib
#Employees department disturbution
Employees["Department"].value_counts().plot(kind="bar")
plt.title("Employees by department")
plt.xlabel("Department")
plt.ylabel("Number of employees")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#Employees Average Salary
department_counts=Employees["Department"].value_counts()
plt.figure(figsize=(10,6))
department_counts.plot(kind="bar")
plt.title("Employee disturbution by department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#projects by status
status_count=projects["Status"].value_counts()
plt.figure(figsize=(8,6))
status_count.plot(kind="bar")
plt.title("Projects by status")
plt.xlabel("Project Status")
plt.ylabel("Number of Projects")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
#projects-total budget vs Revenue
projects["Budget_INR"]=pd.to_numeric(projects["Budget_INR"],errors="coerce")
projects["Revenue_INR"]=pd.to_numeric(projects["Revenue_INR"],errors="coerce")
financials=projects[["Budget_INR","Revenue_INR"]].sum()
plt.figure(figsize=(8,6))
financials.plot(kind="bar")
plt.xlabel("Financial Metric")
plt.ylabel("Amount(INR)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
#Project allocation_total hours by role
allocation["Hours_Worked"]=pd.to_numeric(allocation["Hours_Worked"],errors="coerce")
hours_by_role=(allocation.groupby("Role")["Hours_Worked"].sum().sort_values(ascending=True))
plt.figure(figsize=(10,7))
hours_by_role.plot(kind="bar")
plt.title("Total Hours Worked by Role")
plt.xlabel("Total Hours Worked")
plt.ylabel("Role")
plt.tight_layout()
plt.show()

#project Allocation -Top 10 projects by hours
allocation["Hours_worked"]=pd.to_numeric(allocation["Hours_Worked"],errors="coerce")
top_projects=(allocation.groupby("Project_ID")["Hours_Worked"]
              .sum().sort_values(ascending=False).head(10))
plt.figure(figsize=(10,6))
top_projects.plot(kind="bar")
plt.title("Top 10 Projects by Total Hours Worked")
plt.xlabel("Project")
plt.ylabel("Total Hours Worked")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#==================================================================================================
#IT tickets
#==================================================================================================
#tickets by priority
priority_counts=tickets["Priority"].value_counts()
plt.figure(figsize=(8,6))
priority_counts.plot(kind="bar")
plt.title("IT tickets By Priority")
plt.xlabel("Priority")
plt.ylabel("Number of Tickets")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
#IT tickets-Average resolution time by priority
tickets["Created_date"]=pd.to_datetime(tickets["Created_Date"],errors="coerce")
tickets["Resolved_Date"]=pd.to_datetime(tickets["Resolved_Date"],errors="coerce")
tickets["Resolution_Days"]=(tickets["Resolved_Date"]-tickets["Created_Date"]).dt.days
avg_resolution=(tickets.groupby("Priority")["Resolution_Days"].mean().sort_values())
plt.figure(figsize=(8,6))
avg_resolution.plot(kind="bar")
plt.title("Average Resolution Time By Ticket Priority")
plt.xlabel("Priority")
plt.ylabel("Average Resolution Days")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
#=================================================================================================
#Monthly performance
#=================================================================================================
#monthly performance planned vs actual hours
performance["Planned_Hours"]=pd.to_numeric(performance["Planned_Hours"],errors="coerce")
performance["Actual_Hours"]=pd.to_numeric(performance["Actual_Hours"],errors="coerce")
hours=performance[["Planned_Hours","Actual_Hours"]].sum()
plt.figure(figsize=(8,6))
hours.plot(kind="bar")
plt.title("Total planned hours vs Actual Hours")
plt.xlabel("Hours Category")
plt.ylabel("Total Hours")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
#Monthly performance-Bugs va client Satisfaction
performance["Client_Satisfaction"]=pd.to_numeric(performance["Client_Satisfaction"],errors="coerce")
performance["Bugs"]=pd.to_numeric(performance["Bugs"],errors="coerce")
plt.figure(figsize=(8,6))
plt.scatter(performance["Bugs"],performance["Client_Satisfaction"])
plt.title("Bugs vs client Satisfaction")
plt.xlabel("Number of Bugs")
plt.ylabel("Client Satisfaction")
plt.tight_layout()
plt.show()



