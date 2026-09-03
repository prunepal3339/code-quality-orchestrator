import os
import zipfile
import tarfile

def extract_zip(zip_path, extract_to):
    """Extracts a ZIP file."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {zip_path} to {extract_to}")

def extract_tar(tar_path, extract-to):
    """Extracets a TAR file."""
    if tar_path.endswith('.gz'):
        mode = 'r:gz'
    elif tar_path.endswith('bz2'):
        mode ='r:bz2'
    else:
        mode = "r"
    
    with tarfile.open(tar_path ,mode) as tar_ref:
        tar_ref.extractall(path=extract_to)
    #print(f"Extracting {tar_path} to{extract_to}")

# Example usage
if __name__ == "__main__":
    zip_file_path = 'example.zip'  # Replace with your ZIP file path
    tar_file_path = "example.tar.gz"  # Replace this with your TAR file path
#    extract_zip(zip_file_path, './extracted_files')
#    extract_tar(tар_file_path, "./extracted_files")
