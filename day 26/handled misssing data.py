<<<<<<< HEAD
import pandas as pd

data = {'Name': ['Alice', None, 'Charlie'],
        'Age': [25, None, 35],
        'City': ['New York', 'Los Angeles', None]}
df = pd.DataFrame(data)

# Fill missing values
filled_df = df.fillna('Unknown')
print(filled_df)

# Drop rows with missing values
cleaned_df = df.dropna()
print(cleaned_df)
=======
import pandas as pd

data = {'Name': ['Alice', None, 'Charlie'],
        'Age': [25, None, 35],
        'City': ['New York', 'Los Angeles', None]}
df = pd.DataFrame(data)

# Fill missing values
filled_df = df.fillna('Unknown')
print(filled_df)

# Drop rows with missing values
cleaned_df = df.dropna()
print(cleaned_df)
>>>>>>> ad12eb181427590f30d26fd51061b42124f2f380
