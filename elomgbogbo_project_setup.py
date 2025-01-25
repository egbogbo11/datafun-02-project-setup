"""
Module: elomgbogbo_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Elom Gbogbo


"""

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library

import pathlib
import time

# Import local modules

import utils_gbogbo


#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    
    for year in range(start_year, end_year + 1):
        year_path = data_path.joinpath(str(year))
        year_path.mkdir(exist_ok=True)
        print(f"Folder created: {year_path}")

  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders for a list of names.
    
    Arguments:
    folder_list - A list of folder names to be created.
    to lowercase - Convert folder names to lowercase if True
    remove_spaces - Replace spaces with underscores in folder names in True.
    '''
    print("Creating folders from the provided list...")
    for name in folder_list:
        original_name = name
        if to_lowercase:
            name = name.lower()
        if remove_spaces: name = name.replace(" ", "-")
        folder_path = data_path.joinpath(name)
        folder_path.mkdir(exist_ok=True)
        print(f"Folder created: {folder_path} Original: '{original_name}')")
    


  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Create folders with a given prefix for each name in a list.
    
    Arguments:
    folder_list - A list of folders names to be prefixed and created
    prefix - The prefix to be added to each folder name.
    '''
    
    print(f"Creating folders with prefix '{prefix}'...")
    for name in folder_list:
        prefixed_name = f"{prefix}{name}"
        folder_path = data_path.joinpath(prefixed_name)
        folder_path.mkdir(exist_ok=True)
        print(f"Folder created: {folder_path}")

  

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create a series of folders periodically over a specified duration.
    
    Arguments:
    duration_seconds - The total duration between the created folders
    '''
    for i in range(5):
        folder_name = f"folder{i+1}"
        folder_path = project_path.joinpath(folder_name)
        folder_path.mkdir(exist_ok=True)
        print(f"Folder created: {folder_path}")
        time.sleep(duration_seconds)


  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    
    print(f"Byline: {utils_gbogbo.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.