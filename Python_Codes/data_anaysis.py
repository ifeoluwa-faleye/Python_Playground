!pip install datasets #Installing the dataset module
from datasets import load_dataset
dataset = load_dataset("lukebarousse/data_jobs")
df = dataset["train"].to_pandas() #converts dataset into a pandas dataframe
df.info()
df.head(10)
df.iloc[90:100]
df[['job_title_short','job_title']].head()
df['salary_year_avg'].describe()
df.job_title_short.unique()
df[(df.job_title_short == "Data Analyst") & (df.salary_year_avg.notna())]
df['job_posted_date'] = pd.to_datetime(df.job_posted_date) #converts job_posted_date from string to datetime
df['job_posted_month'] = df.job_posted_date.dt.month #add new column job_posted_month
df.sort_values('job_posted_date', inplace = True) #sort the date by job_posted_date
df.drop('salary_hour_avg', axis = 1, inplace = True) #drop salary_hour_avg column
df.dropna(subset = ['salary_year_avg'], inplace = True) #drops null values for salary_year_avg
min_salary = df['salary_year_avg'].idxmin()
df['job_title_short'].value_counts()
df.groupby('job_title_short')['salary_year_avg'].min().sort_values()
df.groupby(['job_country', 'job_title_short'])['salary_year_avg'].median().sort_values()
df.groupby(['job_title_short','job_country'])['salary_year_avg'].agg(['min','max','median'])
us_jobs = df[df['job_country'] == "United States"]
us_jobs = us_jobs[us_jobs['salary_year_avg'].notna()]
us_jobs.groupby(['job_title_short'])['salary_year_avg'].agg(['sum','mean','median','min','max']).sort_values(by = 'median')
