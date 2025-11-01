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
