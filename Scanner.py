import pandas as pd
import numpy as np
# import tensorflow as tf

# # Read test data CSV file into a DataFrame
# path = 'path/to/your/file/'
# data = pd.read_csv(path + 'test data.csv')

from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "glassdoor"],
    search_term="Data engineer",
    location="Sydney",
    results_wanted=2,
    country_indeed='Australia'  # only needed for indeed / glassdoor
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("C:\Users\James\Python Projects\Data-Engineer-Scanner\jobs.csv", index=False) # to_xlsx
