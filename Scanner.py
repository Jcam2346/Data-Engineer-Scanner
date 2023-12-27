import pandas as pd
import numpy as np
import os
import tensorflow as tf

# Print the current working directory
print(os.getcwd())

from jobspy import scrape_jobs

# Scrape jobs from indeed and glassdoor
jobs = scrape_jobs(
    site_name=["indeed", "glassdoor"],
    search_term="Data engineer",
    location="Sydney NSW",
    results_wanted=15,
    # only needed for indeed / glassdoor
    country_indeed='Australia',
    #proxy="" #must be a string in the format "ip_address:port" starting with http:// or https://
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())

jobs.to_csv("Data-Engineer-Scanner/jobs.csv", index=False)

#
