# Checks if a file already exists
unique_files = []
file_list = ['report.csv', 'data.xlsx', 'summary.docx', 'data.csv',]
for file in file_list:
    if file not in unique_file:
        unique_files.append(file)
    else:
        print(f'{file} is a duplicate')
        break
else:
    print('All files are unique')


#List comprehension exercises, casting string to datetime
from datetime import datetime
data_science_jobs = [
    {'job_title': 'Data Scientist', 'job_skills': "['Python', 'SQL', 'Machine Learning']", 'job_date': '2023-05-12'},
    {'job_title': 'Machine Learning Engineer', 'job_skills': "['Python', 'TensorFlow', 'Deep Learning']", 'job_date': '2023-05-15'},
    {'job_title': 'Data Analyst', 'job_skills': "['SQL', 'R', 'Tableau']", 'job_date': '2023-05-10'},
    {'job_title': 'Business Intelligence Developer', 'job_skills': "['SQL', 'PowerBI', 'Data Warehousing']", 'job_date': '2023-05-08'},
    {'job_title': 'Data Engineer', 'job_skills': "['Python', 'Spark', 'Hadoop']", 'job_date': '2023-05-18'},
    {'job_title': 'AI Specialist', 'job_skills': "['Python', 'PyTorch', 'AI Ethics']", 'job_date': '2023-05-20'}
]

for jobs in data_science_jobs:
    jobs['job_date'] = datetime.strptime(jobs['job_date'], '%Y-%m-%d')
print(data_science_jobs)
