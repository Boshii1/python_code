# Created: by Naotoshi Yoshida
# Modified date : 11-17-2023
# Description: To read a .csv file to find documents that meet a certain criteria that will initiate a copy 
# and store them into a new folder. The program will be able to navigate thru the file directory to pull the corerct files

import pandas as pd 
import shutil
import os.path
from datetime import datetime 

now = datetime.today()

# create a variable that stores the current date 
curr_date = now.strftime('%m-%d-%Y')
print('Current date is : ' + curr_date)

# specify the date, month and year and store them into separate variables 
curr_year = str(now.year)
print(curr_year)
curr_month = str(now.month)
print(curr_month)
curr_day = str(now.day)
print(curr_day)

# create the directory path for the csv files
csv_dirPath = os.path.join(r'\\CTY-MEGABYTE-SQL\tiffimages\NewDeeds') 
print(csv_dirPath)

# create the filename of the csv using the curr_date variable 
# csv_fileName = curr_date + '.csv' 
csv_fileNameTest = curr_date + '.csv'
print(csv_fileNameTest)

# create the filepath by using os.path.join to create the path from csv_dirPath and csv_fileName
csv_filePath = os.path.join(csv_dirPath, csv_fileNameTest)
print(csv_filePath)

# to read from the csv we need to use the pd.read_csv method 
# create a check to read data from csv 
try: 
    data = pd.read_csv(csv_filePath)
    print('File read succesfully!')
except FileNotFoundError: 
    print(f'No file found at {csv_filePath}')
except pd.errors.ParserError:
    print(f'Could not parse the file at {csv_filePath}')
except Exception as e: 
    print(f'An unexpected error occurred: {e}')

# create a variable with all the specific document types to filter 
file_types = ['AF01', 'AF02', 'AF03', 'AF04', 'AF05', 'AF06', 'AF07', 'AFF', 'AG', 
              'CD01', 'CD02', 'CD04', 'CD05', 'CD08', 'CR09', 'CR10', 'DE', 'DE03',
              'DE06', 'DE07', 'DE08', 'DE09', 'FS', 'FS01', 'FS02', 'FS03', 'FS04',
              'FS05', 'FS07', 'GR01', 'GR11', 'LE', 'LE01', 'MI', 'MI03', 'MI14',
              'MI16', 'NT', 'NT01', 'NT02', 'NT06', 'NT09', 'NT11', 'NT21', 'TE',
              'TL', 'TL06']

# create a variable for the filtered document types
filtered_data = data[data['Document' + ' ' + 'Code'].isin(file_types)]
print(filtered_data)

# create a variable with the file path of the folder containing the copies
copy_folder = r'C:\Deeds_for_JA'

# iterate through the rows in the filtered_data dataframe 
for index, row in filtered_data.iterrows(): 
    
    # store the names of the file while iterating through the rows while the path is set 
    source_tiffFile = os.path.join(r'\\CTY-MEGABYTE-SQL\tiffimages\NewDeeds',curr_year,curr_month,curr_day,row['Instrument Number'] + '.txt') 
    print(source_tiffFile)
    try:
        shutil.copy(source_tiffFile, copy_folder)
        print(f'Successfully copied {source_tiffFile} to {copy_folder}')
    except Exception as e:
        print(f'Failed to copy {source_tiffFile} to {copy_folder}. Error: {e}')