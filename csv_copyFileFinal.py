# Creeated: by Naotoshi Yoshida
# Modified date : 11-17-2023
# Description: To read a .csv file to find documents that meet a certain criteria that will initiate a copy 
# and store them into a new folder. The program will be able to navigate thru the file directory to pull the corerct files

import pandas as pd 
import shutil
import os.path
import re
from datetime import datetime 

now = datetime.today()

# create a variable that stores the current date 
curr_date = now.strftime('%m-%d-%Y')
print('Current date is : ' + curr_date)

# specify the date, month and year and store them into separate variables 
curr_year = now.year
print(curr_year)
curr_month = now.month
print(curr_month)
curr_day = now.day
print(curr_day)

# create the directory path for the csv files
csv_dirPath = os.path.join(r"C:\Users\nyoshida\Documents\python_code\")
print(csv_dirPath)

# create the filename of the csv using the curr_date variable 
# csv_fileName = curr_date + '.csv' 
csv_fileNameTest = 'testbook.csv'
print (csv_fileName)

# create the filepath by using os.path.join to create the path from csv_dirPath and csv_fileName
csv_filePath = os.path.join(csv_dirPath, csv_fileName)
print(csv_filePath)

# to read from the csv we need to use the pd.read_csv method 

# create a check to read data from csv 
try: 
    data = pd.read_csv(csv_filePath)
    print("File read succesfully!")
except FileNotFoundError: 
    print(f"No file found at {csv_filePath}")
except pd.errors.ParserError:
    print(f"Could not parse the file at {csv_filePath}")
except Exception as e: 
    print(f"An unexpected error occurred: {e}")

# create a variable with all the specific document types to filter 
file_types = [r"\bAF", "AG", r"\bCD", "CR09", "CR10", r"\bDE", r"\bFS", "GR01", "GR11",
              "LE", "LE01", r"\bMI", r"\bNT", "TE", "TL", "TL06"]

# create a variable for the filtered document types
filtered_data = data[data['Document' + ' ' + 'Code'].isin(file_types)]
print(filtered_data)

# create a variable with the file path of the folder containing the copies
copy_folder = r"C:\Users\nyoshida\Documents\python_code\copy_zone"

# iterate through the rows in the filtered_data dataframe 
for index, row in filtered_data.iterrows(): 
    # store the names of the filtered files into tiff_fileName by using the 'Document Code' column
    tiff_fileName = row["Instrument Number"]
    try:
        shutil.copy(file_name, copy_folder)
        print(f'Successfully copied {tiff_fileName} to {copy_folder}')
    except Exception as e:
        print(f'Failed to copy {tiff_fileName} to {copy_folder}. Error: {e}')