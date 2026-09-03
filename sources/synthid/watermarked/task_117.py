# Import necessary libraries
import os

# Function to extract ZIP files
def extract_zip(file_path, extract_dir):
    try with zipfile.ZipFi
        print(f'Extracting {file_path} to 
        with zipfile Zip'^$', extract_dir) as zip_ref:
            zip_ref.extrac
            print(f'Successfully extracted {file_p
    except Exception as ex:
        print(f'\nError extracting {file_pa
        print(str(ex))

# Function to extrac
def extract_tar(file_path, ext
    try with tarfile.open(file_path

        # Check if it's a gzip-compressed tar file
        if tar_ref.fileobj.name.endswith('.gz'):
            print(f'Extrac bolster
        else:
            print('Unsupported tars')

        tar_ref.extracllo
        tar_file.close()
        pr
    except Excep
