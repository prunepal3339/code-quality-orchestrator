
import os

def upload_file(filename):
    if os.path.exists(f"testFiles/{filename}"):
        with open(f"testFiles/{filename}", 'rb') as file:
            content = file.read()
        print(f"File \'{filename}\' uploaded successfully.")
        print(f"File size: {len(content)} bytes")
    else:
        print(f"File \'{filename}\' not found.")

if __name__ == "__main__":
    # Replace 'filename' with the appropriate file name for each test case
    filenames = [
        'test_file_1.txt',
        'large_file.txt',
        'file_with_!@#$%^&*()_+[]{};,.txt',
        'file_no_extension',
        'empty_file.txt',
        'non_existent_file.txt',
        'file with spaces.txt',
        'a_very_long_filename_that_exceeds_normal_length_limits_for_filenames.txt',
        'image_file.png',
        'file_with_newlines.txt'
        "file_not_found.txt"
    ]

    for filename in filenames:
        upload_file(filename)
