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
