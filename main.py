import pandas as pd
import matplotlib.pyplot as plt

d7= {
    "Name":["Ravi", "Astha","Illisha","Lika","Radha","Ravi","Astha","Liku"], "Email":["r@gmail.com","a@gmail.com","i@gmail.com","l@gmail.com","ra@gmail.com","r@gmail.com","a@gmail.com","l@gmail.com"],
    "Salary":[200.25,140,60.75,80.18,90.15,450,260,65],
    "Age": [39,35,6,3,6,39,35,3],
    "Education": [3,3,1,0,1,3,3,0]

}
df7= pd.DataFrame(d7)
#
#plot graph Vertically and it is the default graph
gf2= df7.plot.bar()
gf2.set_xlabel("X-Axis")
gf2.set_ylabel("Y-Axis")
#
#plot graph horizontally
gf1= df7.plot.barh()
gf1.set_xlabel("X-Axis of Horizontal")
gf1.set_ylabel("Y-Axis of Horizontal")
#
#plot Histogram
gf3= df7.plot.hist()
gf3.set_xlabel("X-Axis of Histogram")
gf3.set_ylabel("Y-Axis of Histogram")
#
#plot Histogram on basis of Age
gf4= df7['Age'].plot.hist()
gf4.set_xlabel("X-Axis of Age Histogram")
gf4.set_ylabel("Y-Axis of Age Histogram")
#
#Another way of plotting Histogram on basis of Age
gf5= df7['Age'].plot(kind ='hist', stacked = True, bins = 100,figsize= (10,10), title ="Histogram of Age", orientation = "horizontal")
gf5.set_xlabel("X-Axis of Age Histogram")
gf5.set_ylabel("Y-Axis of Age Histogram")
#
# #in case we want to plot each element of dataframe individually. i.e age and salary in separate histogram
df7.hist(color= 'red')

#plotting age and salary in separate histogram in a different color
#alpha determines what will be be shade of graph. higher the alpha graph would be more strong in color, lower the alpha graph will be faded in color
df7.hist(color= '#66ff99', alpha = .3)

# #creating a scatter plot based on Age and Salary
df7.plot.scatter(x='Age', y= 'Salary')

# #creating a scatter plot based on Age and Salary
df7.plot.scatter(x='Age', y= 'Salary', c= 'Age',s= 10)

#scatter matrix will give a graph which shows relationship between one element to another element of graph
pd.plotting.scatter_matrix(df7,figsize=(10,10))

# If we need bell curve in the report
pd.plotting.scatter_matrix(df7,figsize=(10,10), diagonal = 'kde')


# creating a hexbin plot based on Age and Salary
df7.plot.hexbin(x='Age', y= 'Salary', label= 'Ravi',gridsize = 10)

# #creating a pie plot based on Salary
df7.plot.pie(y='Salary')

# #creating a pie plot based on Age, Salary and Education
#autopct will give till waht decimal values we want toe data in pie chart. over here 2 decimal values are given
df7[['Age', 'Salary','Education']].plot.pie(subplots= True,fontsize= 8,autopct = '%.2f')


plt.show()