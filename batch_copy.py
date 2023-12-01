# Created by: Naotoshi Yoshida 
# Modified Date: 11-29-2023
# Description: Building on the csv_copy script, this will go in a batch of the date range
# from the date the initial copy should start into the current date. This will mainly function 
# as nested for loops that will iterate through the dates of the csv files and then iterate through
# the cells within the csv to copy the necessary files over. 

import pandas as pd
import shutil 
import os.path 
from datetime import date, timedelta
import glob

# create a variable with all the specific document types to filter 
file_types = ['AF01', 'AF02', 'AF03', 'AF04', 'AF05', 'AF06', 'AF07', 'AFF', 'AG', 
              'CD01', 'CD02', 'CD04', 'CD05', 'CD08', 'CR09', 'CR10', 'DE', 'DE03',
              'DE06', 'DE07', 'DE08', 'DE09', 'FS', 'FS01', 'FS02', 'FS03', 'FS04',
              'FS05', 'FS07', 'GR01', 'GR11', 'LE', 'LE01', 'MI', 'MI03', 'MI14',
              'MI16', 'NT', 'NT01', 'NT02', 'NT06', 'NT09', 'NT11', 'NT21', 'TE',
              'TL', 'TL06']

# create a directory for the source directory 
source_directory = r'\\CTY-MEGABYTE-SQL\tiffimages\NewDeeds'

# create a variable with the file path of the folder containing the copies
copy_folder = r'C:\Deeds_for_JA'

# Goal: is to pass a date value through this
# will extrapolate further the date format, year, month, and day
def get_date(input):
    date = input.strftime('%m-%d-%Y')
    year = str(input.year)
    month = str(input.month)
    day = str(input.day)
    return date, year, month, day

# Function date_range returns the days 
# in between two dates should print in the format ('%m-%d-%Y)
# Note: is not inclusive of the last date, 
# will need to add one more date to accomodate for the range
def date_range(start_date, end_date):
    for n in range (int((end_date - start_date).days)):
        yield start_date + timedelta(n)

# These two variables will be used for the range of dates needed to get the correct csvs and
# get the proper file path of the tiff images
start_date = date(2023, 8, 1)
end_date = date(2023, 8, 30)


# this will be the for loop that will loop through the dates and set those date values into
# variables to use for the csv file name and the file path
for single_date in date_range(start_date, end_date):
    curr_date, curr_year, curr_month, curr_day = get_date(single_date)
    
    # create the filename of the csv using the curr_date variable 
    csv_fileNameTest = curr_date + '.csv'
    print(csv_fileNameTest)
    # create the filepath by using os.path.join to create the path from csv_dirPath and csv_fileName
    csv_filePath = os.path.join(source_directory, csv_fileNameTest)
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

    # create a variable for the filtered document types
    filtered_data = data[data['Document' + ' ' + 'Code'].isin(file_types)]
    # iterate through the rows in the filtered_data dataframe 
    for index, row in filtered_data.iterrows(): 
        
        # store the names of the file while iterating through the rows while the path is set 
        # may be able to separate the folder and text file rather than having to encase the file into one file path
        specific_tif = os.path.join(source_directory,curr_year,curr_month,curr_day,row['Instrument Number'])
        source_tifFile = glob.glob(os.path.join(source_directory,curr_year,curr_month,curr_day,specific_tif + '*.txt'))
        print(source_tifFile)
        try:
            shutil.copy(source_tifFile, copy_folder)
            print(f'Successfully copied {source_tifFile} to {copy_folder}')
        except Exception as e:
            print(f'Failed to copy {source_tifFile} to {copy_folder}. Error: {e}')