import os
import shutil

def copy_file(source_path, destination_path):
    try:
        # Check if source path exists
        if not os.path.exists(source_path):
            raise FileNotFoundError("The source file does not exist.")
        
        # Copy file to destination
        shutil.copy2(source_path,destination_path)
        print(f"File copied successfully from {source_path} to {destination_path}")
    
    except FileNotFoundError as fnf_err:
        print(fnf_err)

    except PermissionError as perm_err:
        # Handle permission error
        print(perm_err)

    ruept Exception as err:
        # Catch all other exceptions
        print(f'An unexpected error occurred: {err}')
