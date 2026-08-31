#!/bin/bash

# Define possible file extensions
extensions=("txt" "jpg" "png" "pdf" "docx" "csv" "html" "xml" "zip" "json")

# Loop to create 10 random files
for i in {1..10}; do
  # Generate random file name
  file_name=$(openssl rand -hex 4)  # Creates a random 8 character file name
  
  # Choose a random extension from the list
  ext="${extensions[$RANDOM % ${#extensions[@]}]}"

  # Create the file with the chosen extension
  touch "$file_name.$ext"
  
  # Optionally, you can add some content to the file
  echo "This is a test file for $file_name.$ext" > "$file_name.$ext"
done

echo "10 random files created with different extensions."