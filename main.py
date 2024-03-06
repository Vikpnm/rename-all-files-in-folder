import os

# Define the folder path where files will be renamed
folder_path = ""


# Function to rename files in the specified folder
def rename_files(folder_path):
    # Get the list of files in the specified folder
    files = os.listdir(folder_path)

    # Initialize a counter to track the renaming process
    count = 1

    # Iterate through each file in the folder
    for file_name in files:
        # Get the full path of the current file
        old_file_path = os.path.join(folder_path, file_name)

        # Extract the file extension
        file_extension = os.path.splitext(file_name)[1]

        # Create a new file name with the format "Untitled {count}.{file_extension}"
        new_file_name = f"Untitled {count}{file_extension}"

        # Create the full path for the new file name
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file by moving it to the new file path
        os.rename(old_file_path, new_file_path)

        # Increment the counter for the next file
        count += 1


# Call the function to rename files in the specified folder
rename_files(folder_path)
