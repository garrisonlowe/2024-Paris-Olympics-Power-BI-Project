import kaggle
import os
import pandas as pd

# Set Kaggle API credentials directory
os.environ['KAGGLE_CONFIG_DIR'] = r'C:\Users\garri\.kaggle'

# Setting the dataset identifier in Kaggle
dataset = 'piterfm/paris-2024-olympic-summer-games'

# Set the download path for the csv data files
download_path = r'C:\Users\garri\OneDrive\Desktop\Paris Olympics Power Bi Python Project\Datasets\\'

# Remove existing files in the folder to prevent duplicates or outdated files
for file in os.listdir(download_path):
    file_path = os.path.join(download_path, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
            print(f"Deleted {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")
        
# Download the dataset using the kaggle API and unzip the files.
kaggle.api.dataset_download_files(dataset= dataset, path= download_path, unzip= True)

# List of csv files to be imported
csv_files = ['athletes.csv',
             'events.csv',
             'coaches.csv',
             'medallists.csv',
             'medals.csv',
             'medals_total.csv',
             'nocs.csv',
             'schedules.csv',
             'schedules_preliminary.csv',
             'teams.csv',
             'technical_officials.csv',
             'torch_route.csv',
             'venues.csv']

# Initialize a directory to hold the DataFrames
dataframes = {}

# Iterate through each CSV files and load it into a DataFrame
for file in csv_files:
    #Construct the full path to the CSV file
    file_path = os.path.join(download_path, file)
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Add the DataFrame to the dictionary using the file name as the key
    table_name = file.split('.')[0] 
    dataframes[table_name ]= df