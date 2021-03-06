# lab11.6.createdata.py
# Author David


import pandas as pd

listdata = [
    ['John', 'maths',       23],
    ['John', 'programming', 66],
    ['Mary', 'maths',       45],
    ['Mary', 'programming', 33],
    ['Mark', 'maths',       57],
    ['Mark', 'programming', 70],
    ['Pete', 'maths',       73],
    ['Pete', 'programming', 61]
]


df = pd.DataFrame(listdata, columns=['name','subject','grade'])
print(df.head(3))

print(df.describe())
print(type(df.describe()))


# Write file to csv
path = "./data/"
csvfilename = path +  'grades.csv'
df.to_csv(csvfilename)


# Write an excel file
excelfilename = path + 'grades.xlsx'
df.to_excel(excelfilename, index=False, sheet_name='data')
with pd.ExcelWriter(excelfilename, engine='openpyxl', mode='a') as writer:
    df.describe().to_excel(writer, sheet_name="summary")


# Calculte and print the mean of the grades
mean = df.describe().loc['mean','grade']
print(mean)
# or 
mean = df['grade'].mean()
print(mean)
