import pandas as pd 
import shutil 
import os.path
from datetime import datetime 

# store the date as a global variable 
now = datetime.now()

#store the date values into separate variables 
curr_day = now.day()
curr_month = (now.month() + ' ' + now.strftime('%B'))
curr_year = now.year()

print("Current month:", curr_month)

curr_date = datetime.today().strftime('%m-%d-%Y')
print("This is the current date:" + curr_date)

# create a directory path with the date variables 
dir_path = os.path.join(r'C:\Users\nyoshida\Documents\python_code',curr_year,curr_month,curr_day) 
print(dir_path)

# create a file name for the csv file using the curr_date variable 
file_name = curr_date + '.csv'
print(file_name)

# create the path for the read_csv method 
file_path = os.path.join(dir_path, file_name)
print(file_path)

# read data from csv
try:
    data = pd.read_csv(file_path)
    print("File read successfully!")
except FileNotFoundError:
    print(f"No file found at {file_path}")
except pd.errors.ParserError:
    print(f"Could not parse the file at {file_path}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# set file_types to read for specific values
file_types = ['Deeds', 'PCORS', 'Affidavit']

# filter the rows where the column 'Type' is in file_types 
filtered_data = data[data['Type'].isin(file_types)]

# print table of filtered rows 
# print(filtered_data)

# create a variable with the file path of the folder containing the copies 
copy_folder = r"C:\Users\nyoshida\Documents\python_code\copy_zone"

# # iterate through the rows in the filtered_data
# for index, row in filtered_data.iterrows(): 
#     # store the names of the filtered files into file_name by using the column name 
#     file_name = row['Name']
#     # check statement for copying the filtered files into the new folder 
#     try:
#         shutil.copy(file_name, copy_folder)
#         print(f'Successfully copied {file_name} to {copy_folder}')
#     except Exception as e:
#         print(f'Failed to copy {file_name} to {copy_folder}. Error: {e}')
