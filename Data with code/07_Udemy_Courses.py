import numpy as np
import pandas as pd
import seaborn as sns


data= pd.read_csv("C:\\Users\\manish\\Desktop\\Datasets\\07_Udemy_Courses.csv")
data.info()
"pd.drop(data[""])"

"1. For how must subjects udemy is giving the courses"
data["subject"].unique()

"2. Subject that has the max no.of coures"
data["subject"].max()

"3. Counts the value of each subject in series data"
data["subject"].value_counts()

"4. Show all the courses which free of cost"
Free_course=data[data.is_paid== False].count()
Free_course=data[data.is_paid== True]
data[data.is_paid== True].count()

"5. Course Wih most subscriber"
data.sort_values(by= ['num_subscribers'], ascending = False).head()

"6. Course Wih most subscriber"
data.sort_values(by= ['num_subscribers']).head()

"7. Graphic Designs course with price below 100rs "
len(data[(data.subject=="Graphic Design") & (data.price<="100")].count())

"8. List All the courses related to python"
len(data[data.course_title.str.contains("Python")])

"9. Coures that published in 2015"
data.dtypes
data['published_timestamp']=pd.to_datetime(data['published_timestamp'])
data.dtypes
data['years']=data['published_timestamp'].dt.year
len(data[data.years==2015])

"10. max no. of subscriberes in each level of course"
data.groupby('level')["num_subscribers"].max()
data.groupby('level')["num_subscribers"].min()


