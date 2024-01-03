import pandas as pd
import numpy as np
import os
import tensorflow as tf

print(os.getcwd())

# Scrape jobs from indeed and glassdoor
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "glassdoor"],
    search_term="Data engineer",
    location="Sydney NSW",
    results_wanted=15,
    # only needed for indeed / glassdoor
    country_indeed='Australia'#,
    #proxy="" #must be a string in starting with http:// or https:// and may end in format "ip_address:port" 
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())

jobs.to_csv("Data-Engineer-Scanner/jobs.csv", index=False)

#
