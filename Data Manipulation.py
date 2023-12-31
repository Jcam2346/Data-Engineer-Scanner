import pandas as pd
import os

# Read the CSV file into a pandas dataframe
print(os.getcwd())
df = pd.read_csv('Kaggle Dataset.csv', encoding='utf-8')

# Print the first 3 rows of the dataframe
print(len(df))

# Filter df to include only rows with 'Data' and 'Engineer' in the Job Title column
new_df = df[df['Job Title'].str.contains('(?i)data') & df['Job Title'].str.contains('(?i)engineer') & ~df['Job Title'].str.contains('(?i)software')]

# Print the number of rows in the new dataframe
print(len(new_df))
print(new_df.head(15))
