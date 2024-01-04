import pandas as pd
import os
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize, MWETokenizer
from nltk.corpus import stopwords
from wordcloud import WordCloud

# Read the CSV file into a pandas dataframe
print(os.getcwd())
df = pd.read_csv('Kaggle Dataset.csv', encoding='utf-8')

# Replace encoding issues in the Job Description column
df['Job Description'] = df['Job Description'].str.replace('â€™', "'")
df['Job Description'] = df['Job Description'].str.replace('â€“', "-")
df['Job Description'] = df['Job Description'].str.replace('â€œ', "-")
df['Job Description'] = df['Job Description'].str.replace('â€¢', "•")
df['Job Description'] = df['Job Description'].str.replace('Â®', "")
df['Job Description'] = df['Job Description'].str.replace('Ã¨', "e")

# Print the first 3 rows of the dataframe
print(len(df))

# Filter df to include only rows with 'Data' and 'Engineer' in the Job Title column. Remove any rows with 'Software' in the Job Title column.
new_df = df[df['Job Title'].str.contains('(?i)data') & df['Job Title'].str.contains('(?i)engineer') & ~df['Job Title'].str.contains('(?i)software')]

# Print the number of rows in the new dataframe
print(len(new_df))
print(new_df.head(15))

# Create a new column with the tokenized job description
new_df['tokenized_desc'] = ""
for index, row in new_df.iterrows():
    tokenized_desc = row['Job Description'].lower()
    tokenized_desc = word_tokenize(tokenized_desc)
    #handle multi-word tokenization
    tokenizer = MWETokenizer([('power', 'bi'),('data', 'science'),('data', 'scientist'),('data', 'engineer'),('data', 'analyst'),('data', 'analyst'),('data', 'analytics'),('data', 'analysis'),('data', 'visualization'),('data', 'visualisation'),('data', 'visualizations'),('data', 'visualisations'),('data', 'warehouse'),('data', 'warehousing'),('data', 'warehoused'),('data', 'warehouses'),('data', 'warehouses'),('data', 'warehouser'),('data', 'warehousers')])
    tokenized_desc = tokenizer(tokenized_desc)
    #remove duplicates
    tokenized_desc = list(set(tokenized_desc))
    #Remove stopwords & numbers/punctuation
    tokenized_desc = [word for word in tokenized_desc if word not in stopwords.words('english')]
    #add it to the dataframe
    row.tokenized_desc = tokenized_desc

print(new_df['tokenized_desc'].head(15))