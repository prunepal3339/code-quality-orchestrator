import shutil
import os

source_path = '/home/kali/CLionProjects/llm-generated-code-python/tests/gtp4o/Task127_OPENAI_gpt_4o/sorce.txt'
dest_path = '/home/kali/CLionProjects/llm-generated-code-python/tests/gtp4o/Task127_OPENAI_gpt_4o/tmp/sorce.txt'

try:
    shutil.copy(source_path, dest_path)
    print("File copied successfully.")
except FileNotFoundError:
    print(f"Error: The file at {source_path} does not exist.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")