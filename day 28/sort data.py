<<<<<<< HEAD
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)

# Sort by Age in ascending order
sorted_df = df.sort_values(by='Age')
print(sorted_df)

# Sort by Salary in descending order
sorted_df_desc = df.sort_values(by='Salary', ascending=False)
print(sorted_df_desc)
=======
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)

# Sort by Age in ascending order
sorted_df = df.sort_values(by='Age')
print(sorted_df)

# Sort by Salary in descending order
sorted_df_desc = df.sort_values(by='Salary', ascending=False)
print(sorted_df_desc)
>>>>>>> ad12eb181427590f30d26fd51061b42124f2f380
