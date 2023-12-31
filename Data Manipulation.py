import pandas as pd

# Read the CSV file into a pandas dataframe
df = pd.read_csv('/c:/Users/James/Python Projects/Data-Engineer-Scanner/Kaggle Dataset.csv', encoding='utf-8')

# Print the first 3 rows of the dataframe
print(df.head(3))
