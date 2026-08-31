import zipfile

def extract_zip(zip_file, extract_dir):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

def extract_tar(tar_file, extract_dir):
    import tarfile
    with tarfile.TarFile(tar_file, 'r') as tar_ref:
        tar_ref.extractall(extract_dir)

# Example usage:
extract_zip('testZip.zip', './testZip')
extract_tar('testTar.tar', './testTar')